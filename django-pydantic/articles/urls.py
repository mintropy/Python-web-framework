from django.urls import path

from .views.article import ArticleViewSet


article_list = ArticleViewSet.as_view({
    'get': 'list'
})
article_detail = ArticleViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', article_list),
    path('<int:article_id>/', article_detail),
]

