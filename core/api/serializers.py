from rest_framework.serializers import ModelSerializer
from core.models import TuristicPoints

# Serializers - filter fields
class TurisiticPointsSerializer(ModelSerializer):
    """ Filtro dos valores retornados - Core """
    class Meta:
        model = TuristicPoints
        fields = ('id', 'name', 'description', 'approved')