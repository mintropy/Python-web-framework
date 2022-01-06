from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, render
# from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoView(APIView):
    
    def get(self, request):
        todos = get_list_or_404(Todo)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
