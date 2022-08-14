from django.contrib import admin

from .models import Article, Reply


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class ReplyInline(admin.TabularInline):
        model = Reply

    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("title",)
    inlines = [ReplyInline]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "article",
        "created_at",
        "updated_at",
    )
