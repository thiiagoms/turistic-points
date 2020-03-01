from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from core.models import TuristicPoints
from core.api.serializers import TurisiticPointsSerializer

# viewset
class TuristicPointsViewSet(ModelViewSet):
    """ Viewset da API """
    serializer_class = TurisiticPointsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    lookup_field = 'name'

    
    def get_queryset(self):
        return TuristicPoints.objects.filter(approved=True)