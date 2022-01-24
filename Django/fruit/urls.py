from django.urls import path
from strawberry.django.views import AsyncGraphQLView, GraphQLView

from .schema import schema
from . import views


urlpatterns = [
    path("graphql/sync/", GraphQLView.as_view(schema=schema)),
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
    path('', views.FruitView.as_view())
]