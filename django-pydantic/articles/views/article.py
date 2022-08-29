from datetime import datetime

from django.shortcuts import get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models import Article
from ..schmas.article import ArticleListSchema, ArticleDetailSchema


class ArticleViewSet(ViewSet):
    model = Article
    queryset = Article.objects.all()

    def list(self, request):
        articles = (
            Article.objects.all()
            .annotate(replies_count=Count("replies"))
            .values("id", "title", "created_at", "replies_count")
        )
        response = [ArticleListSchema(**article) for article in articles]
        return Response(response)

    def create(self, request):
        time_now = datetime.now()
        prev_id = Article.objects.all().order_by("-id").values("id")[0]["id"]
        data = {
            "id": prev_id + 1,
            "title": request.data.get("title", None),
            "content": request.data.get("content", None),
            "created_at": time_now,
            "updated_at": time_now,
        }
        article_schema = ArticleDetailSchema(**data)
        try:
            Article.objects.create(**article_schema.dict())
            return Response(article_schema.dict(), status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article_schema = ArticleDetailSchema(**article.__dict__)
        return Response(article_schema.dict())
