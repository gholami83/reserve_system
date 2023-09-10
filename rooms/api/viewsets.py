from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from ..models import Room,RoomChoice
from .serializers import RoomSerializer,RoomChoiceSerializer,ReserveRoomSerializer


class RoomViewSets(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomChoiceViewSets(ModelViewSet):
    queryset = RoomChoice.objects.all()
    serializer_class = RoomChoiceSerializer


class ReserveRoomViewSets(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = ReserveRoomSerializer
    permission_classes = [IsAuthenticated]
