from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.todo
