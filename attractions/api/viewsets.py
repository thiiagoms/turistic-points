from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from attractions.models import Attractions
from attractions.api.serializers import AttractionsSerializer


# Viewsets here
class AttractionsViewSet(ModelViewSet):
    """ Viewset das aplicações """
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('name', 'description')
    