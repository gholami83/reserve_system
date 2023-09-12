from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import UsersSerializer,CreateHotelSerializer,CreateRoomSerializer,ReserveRoomSerializer
from ..models import Admin,Hotel,Room


class UsersViewSets(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]


class CreateHotelViewSets(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = CreateHotelSerializer


class CreateRoomViewSets(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer
    

class ReserveRoomViewSets(ModelViewSet):
    queryset = Room.objects.filter(reserved = True)
    serializer_class = ReserveRoomSerializer
