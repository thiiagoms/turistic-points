from rest_framework.viewsets import ModelViewSet
from locations.api.serializers import LocationsSerializer
from locations.models import Locations


class LocationsViewSet(ModelViewSet):
    """ Viewset de todas as localizações """
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer