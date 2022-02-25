from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models import Article
from ..schmas.article import ArticleListSchema, ArticleDetailSchema


class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = Article.objects.all().annotate(replies_count=Count('replies'))\
            .values('id', 'title', 'created_at', 'replies_count')
        response = [
            ArticleListSchema(**article) for article in articles
        ]
        return Response(response)

    def retrieve(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article_schema = ArticleDetailSchema(**article.__dict__)
        return Response(article_schema.dict())
