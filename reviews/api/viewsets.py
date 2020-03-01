from rest_framework.viewsets import ModelViewSet
from reviews.models import Reviews
from reviews.api.serializers import ReviewsSerializer


class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer