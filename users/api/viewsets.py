from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from ..models import Hotel, Room
from .permisions import IsReservePermision
from .serializers import (
    CreateHotelSerializer,
    CreateRoomSerializer,
    ReserveRoomSerializer,
)


class CreateHotelViewSets(ModelViewSet):
    serializer_class = CreateHotelSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Hotel.objects.filter(user = self.request.user)


class CreateRoomViewSets(ModelViewSet):
    number = None
    def get_serializer_class(self):
        if self.action in [
            'reserve',
        ]:
            return ReserveRoomSerializer
        else:
            return CreateRoomSerializer    

    def get_queryset(self):
        hotel_id = self.kwargs.get('pk2')
        return Room.objects.filter(hotel_id=hotel_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()

        if self.action in [
            'reserve',
        ]:
            context.update(
                {
                    'room_number' : self.number,
                },
            )
        else:
            context.update(
                {
                    'hotel_id': self.kwargs.get('pk2'),
                },
            )
        return context
    
    def get_permissions(self):
        if self.action in [
            'reserve',
        ]:
            return [
                IsReservePermision(),
                IsAuthenticated(),
            ]
        else:
            return [
                IsAuthenticated(),
            ]
    
    @action(detail=True, methods=['post'])
    def reserve(self,request,pk2,pk):
        room = Room.objects.get(pk=pk)
        self.number = room.room_number
        serializer = ReserveRoomSerializer(room,data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)