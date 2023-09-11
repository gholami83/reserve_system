from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import UsersSerializer,CreateHotelSerializer,CreateRoomSerializer
from ..models import Admin,Hotel,Room


class UsersViewSets(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = UsersSerializer


class CreateAdminViewSets(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = CreateHotelSerializer

class CreateRoomViewSets(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = CreateRoomSerializer
        