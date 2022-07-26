from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from ..models import Article, Reply
from ..serializers.reply import ReplySerializer


class ReplyViewSet(ViewSet):
    model = Reply
    queryset = Reply.objects.all()

    def list(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        replies = get_list_or_404(Reply, article=article)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)

    def create(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        data = {"article": article_id, "content": request.data.get("content", None)}
        serializer = ReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
