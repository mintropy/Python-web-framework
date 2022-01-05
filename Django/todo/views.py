from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo

# Create your views here.
class TodoView(ListView):
    model = Todo
    
    def get(self, request):
        response = JsonResponse(
            self.model.objects.all()
        )
        return response