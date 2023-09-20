from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.decorators import action

from ..models import Hotel,Room


class CreateHotelSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = [
            'id',   
            'name',
            'address',
            'phone',
            'user',
        ]

    def get_user(self,instance):
        return instance.user.username

    def create(self, validated_data):
        validated_data.update({
            "user" : self.context['request'].user,
        })
        return super().create(validated_data)


class CreateRoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id',
            'hotel',
            'room_number',
            'until_reserve',
        ]
    
    def get_hotel(self,instance):
        return instance.hotel.name
        
    def get_room_number(self, instance):
        return instance.room_number

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)

        view = self.context.get('view')
        if view.action in [
            'retrieve',
            'list',
        ]:
            self.fields["room_number"] = serializers.SerializerMethodField(read_only= True)

    def create(self, validated_data):
        hotel_id = self.context.get('hotel_id')
        room_number = self.context.get('room_number')
        validated_data.update(
        {
            "room_number":room_number,
            "hotel_id":hotel_id,
        },
    )
        return super().create(validated_data)


class ReserveRoomSerializer(ModelSerializer):
    room_number = serializers.SerializerMethodField(read_only = True)
        
    def get_room_number(self,instance):
        return instance.room_number
    
    class Meta:
        model = Room
        fields = [
            'reserver_name',
            'room_number',
            'until_reserve',
        ]

    def create(self, validated_data):
        room = Room.objects.get(room_number = validated_data.get('room_number'))
        room.reserver_name = validated_data.get('reserver_name')
        room.until_reserve = validated_data.get('until_reserve')
        room.save()
        return room
    
    def update(self, instance, validated_data):
        instance.reserver_name = validated_data.get('reserver_name', instance.reserver_name)
        instance.until_reserve = validated_data.get('until_reserve', instance.until_reserve)
        instance.save()
        return instance