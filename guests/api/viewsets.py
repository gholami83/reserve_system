from rest_framework.viewsets import ModelViewSet
from ..models import Guest
from .serializers import GuestSerializer


class GuestViewSets(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    
    