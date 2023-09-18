from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateHotelSerializer,CreateRoomSerializer,ReserveRoomSerializer
from ..models import Hotel,Room


class CreateHotelViewSets(ModelViewSet):
    serializer_class = CreateHotelSerializer
    def get_queryset(self):
        return Hotel.objects.filter(user = self.request.user)


class CreateRoomViewSets(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer
    

class ReserveRoomViewSets(ModelViewSet):
    queryset = Room.objects.filter(reserved = True)
    serializer_class = ReserveRoomSerializer
