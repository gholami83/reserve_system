from rest_framework.viewsets import ModelViewSet
from ..models import Reserve
from .serializers import ReserveSerializer


class ReserveViewSets(ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

