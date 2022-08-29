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

    def update(self, request, article_id, reply_id):
        reply = get_object_or_404(Reply, id=reply_id)
        if reply.article.id != article_id:
            return Response()
        data = {"article": article_id, "content": request.data.get("content", None)}
        serializer = ReplySerializer(reply, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, article_id, reply_id):
        reply = get_object_or_404(Reply, id=reply_id)
        if reply.article.id != article_id:
            return Response()
        reply.delete()
        return Response()
