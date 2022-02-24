from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models import Article
from ..schmas.article import ArticleListSchema


class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = Article.objects.all()
        articles_schema = ArticleListSchema.from_django(articles, many=True)
        return Response([article_schema.dict()] for article_schema in articles_schema)

    def retrieve(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article_schema = ArticleListSchema(article)
        return Response(article_schema.dict())
