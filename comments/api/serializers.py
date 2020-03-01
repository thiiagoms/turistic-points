"""
 Serializer dos comentários
"""
from rest_framework.serializers import ModelSerializer
from comments.models import Comments


# Class Serializer
class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user_comment', 'date')