from django.contrib import admin

from .models import Article, Reply


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass
