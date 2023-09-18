from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueForDateValidator
from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Hotel,Room



class CreateHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [
            'name',
            'address',
            'phone',
        ]


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'room_number',
            'reserver_name',
            'date_reserve',
            'reserved',
        ]
    def update(self, instance, validated_data):
        if validated_data.get('reserved'):
            instance.date_reserve = validated_data.get('date_reserve',instance.date_reserve)
        else:
            instance.date_reserve = None
        instance.reserver_name = validated_data.get('reserver_name',instance.reserver_name)
        instance.date_reserve = validated_data.get('date_reserve',instance.date_reserve)
        instance.date_unreserved = validated_data.get('date_unreserved',instance.date_unreserved)
        instance.save()
        return instance
    
    def get_date_reserve(self,instance):
        return instance.date_reserve
    
    def get_room_number(self,instance):
        return instance.room_number

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance,**kwargs)

        view = self.context.get('view')
        if view.action in [
            'retrieve',
            'list',
        ]:
            self.fields["date_reserve"] = serializers.SerializerMethodField()
            self.fields["room_number"] = serializers.SerializerMethodField(read_only = True)
                

        validators = [  
    ]
class ReserveRoomSerializer(ModelSerializer):
    date_unreserved = serializers.SerializerMethodField(read_only = True)
    def get_date_unreserved(self,instance):
        return instance.date_unreserved
    
    class Meta:
        model = Room
        fields = [
            'reserver_name',
            'room_number',
            'date_reserve',
            'date_unreserved',
        ]

    # def create(self, validated_data):
    #     reserve = validated_data.get('reserved')

    #     return isinstance