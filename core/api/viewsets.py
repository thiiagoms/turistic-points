from rest_framework.viewsets import ModelViewSet
from core.models import TuristicPoints
from core.api.serializers import TurisiticPointsSerializer


# viewset
class TuristicPointsViewSet(ModelViewSet):
    """ Viewset da API """
    serializer_class = TurisiticPointsSerializer


    def get_queryset(self):
        return TuristicPoints.objects.filter(approved=True)