from rest_framework import serializers

from ..models import Article


class ArticleListSerialzier(serializers.ModelSerializer):
    replies_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at', 'replies_count',)


class ArticleDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
