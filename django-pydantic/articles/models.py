from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="replies",
        on_delete=models.CASCADE,
    )
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
