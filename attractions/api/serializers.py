from rest_framework.serializers import ModelSerializer
from attractions.models import Attractions 


class AttractionsSerializer(ModelSerializer):
    """ Filtro das atrações """
    class Meta:
        model = Attractions
        fields = ('id', 'name', 'description', 'age', 'open_hour', 'close_hour')
