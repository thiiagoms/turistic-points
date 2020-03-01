from rest_framework.serializers import ModelSerializer
from reviews.models import Reviews


class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('user_review', 'comments', 'description', 'date')