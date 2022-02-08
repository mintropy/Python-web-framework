from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from strawberry.django.views import AsyncGraphQLView, GraphQLView

from .schema import schema
from . import views


# router = DefaultRouter()
# router.register(r'filter', views.FruitFliterView)

urlpatterns = [
    path("graphql/sync/", GraphQLView.as_view(schema=schema)),
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
    path('', views.FruitView.as_view()),
    # path('', include(router.urls))
    path('fruit-search/', views.FruitFliterView.as_view())
]