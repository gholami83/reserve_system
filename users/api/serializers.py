from django.contrib.auth import get_user_model
from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Hotel,Admin,Room


class UsersSerializer(ModelSerializer):
    def get_user(self,instance):
        return {
            'username' : instance.user.username,
            'email' : instance.user.email
        }

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance,**kwargs)

        view = self.context.get('view')
        if view.action in [
            'retrieve',
            'list',
        ]:
            self.fields["user"] = serializers.SerializerMethodField()
    class Meta:
        model = Admin
        fields = [
            'user',
        ]

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
        ]

class ReserveRoomSerializer(ModelSerializer):
    reserved = serializers.SerializerMethodField()
    date_unserved = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        model = Room
        fields = [
            'name'
            'room_number',
            'date_reserve',

        ]
    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)

        Room.reserved = True

# room_number = mo
# date_reserve = 
# reserved = models
# date_unreserved 