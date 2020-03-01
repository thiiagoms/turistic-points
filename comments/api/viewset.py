from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentsSerializer
from comments.models import Comments


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer