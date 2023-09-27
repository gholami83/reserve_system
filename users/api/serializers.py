import pytz
import datetime
import time
from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
    # hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    until_reserve = serializers.DateTimeField(read_only=True)
    reserver_name = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset= Room.objects.all(),
                fields=['hotel','room_number'],
            ),
        ]
        # extra_kwargs = {'until_reserve': {'validator': validate_until_reserve}}
        model = Room
        fields = [
            'id',
            'hotel',
            'reserver_name',
            'room_number',
            'until_reserve',
        ]

    def get_hotel(self,instance):
        return {
            'id':instance.hotel.id,
            'name':instance.hotel.name
        }

        
    def get_room_number(self, instance):
        return instance.room_number
    
    def get_until_reserve(self, instance):
        return instance.until_reserve
   
    def get_reserver_name(self, instance):
        return instance.reserver_name

    def to_internal_value(self, data):
        data = data.copy() 
        hotel_id = self.context['view'].kwargs.get('pk2')
        data['hotel'] = hotel_id
        return super().to_internal_value(data)
        
    def create(self, validated_data):
        hotel_id = self.context.get('hotel_id')
        hotel = Hotel.objects.get(pk=hotel_id)
        room_number = validated_data['room_number']
        validated_data.update(
        {
            "room_number":room_number,
            "hotel":hotel,
        },
    )
        return super().create(validated_data)

    def __init__(self, *args, **kwargs):
        super(CreateRoomSerializer, self).__init__(*args, **kwargs)
        

        view = self.context.get('view')
        if view.action in [
            'retrieve',
            'list',
        ]:
            self.fields["room_number"] = serializers.SerializerMethodField()
            self.fields["hotel"] = serializers.SerializerMethodField()



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

    def validate_until_reserve(self, until_reserve):
        london_tz = pytz.timezone('Europe/London')
        tehran_timezone = pytz.timezone('Asia/Tehran')
        current_timestamp = time.time()
        current_datetime = pytz.utc.localize(datetime.datetime.utcfromtimestamp(current_timestamp)).astimezone(tehran_timezone)
        until_reserve_tehran = until_reserve.astimezone()
        current_datetime = current_datetime + datetime.timedelta(hours=3,minutes=30 )
        current_datetime = current_datetime.timestamp()
        until_reserve_tehran = until_reserve.timestamp()
        print(current_datetime)
        print(until_reserve_tehran)

        if current_datetime > until_reserve_tehran:
            raise serializers.ValidationError("until_reserve should be after now!")
        return until_reserve