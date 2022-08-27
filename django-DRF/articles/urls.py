from django.urls import path

from .views.article import ArticleViewSet
from .views.replies import ReplyViewSet


article_list = ArticleViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
article_detail = ArticleViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)

reply_list = ReplyViewSet.as_view({"get": "list", "post": "create"})
reply_detail = ReplyViewSet.as_view({"put": "update", "delete": "destroy"})

urlpatterns = [
    path("", article_list, name="article list"),
    path("<int:article_id>/", article_detail, name="article detail"),
    path("<int:article_id>/replies/", reply_list),
    path("<int:article_id>/replies/<int:reply_id>/", reply_detail),
]
