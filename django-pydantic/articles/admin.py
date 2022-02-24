from django.contrib import admin

from .models import Article, Reply

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass
