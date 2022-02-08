from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework import generics
from rest_framework import filters
from djangorestframework_camel_case.parser import CamelCaseJSONParser
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Fruit
from .serializers import FruitSerializer

class FruitFilter(django_filters.FilterSet):
    class Meta:
        model = Fruit
        fields = ('name', 'color',)


class CustomCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscorize = {'no_underscore_before_number': True}


# Create your views here.
class FruitView(APIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    render_classes = [CamelCaseJSONRenderer]
    parser_classes = [CamelCaseJSONParser]
    
    def get(self, request):
        fruits = Fruit.objects.all()
        serializer = FruitSerializer(fruits, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FruitFliterView(generics.ListAPIView):
    # queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    
    def get_queryset(self):
        queryset = Fruit.objects.all()
        return queryset
