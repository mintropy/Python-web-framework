from rest_framework.serializers import Serializer, ModelSerializer

from ..models import Reply


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"
