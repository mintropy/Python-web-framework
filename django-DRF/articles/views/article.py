from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import status

from ..models import Article
from ..serializers.article import ArticleListSerialzier, ArticleDetailSerializer


class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = Article.objects.all().annotate(replies_count=Count("replies"))
        serializer = ArticleListSerialzier(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = {
            "title": request.data.get("title", None),
            "content": request.data.get("content", None),
        }
        serializer = ArticleDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, requset, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def update(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def destroy(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response()
