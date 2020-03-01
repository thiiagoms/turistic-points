from rest_framework.serializers import ModelSerializer
from locations.models import Locations


class LocationsSerializer(ModelSerializer):
    """ Serializer para localizações """
    class Meta:
        model = Locations
        fields = ('row', 'city', 'state', 'country', 'latitude', 'longitude')