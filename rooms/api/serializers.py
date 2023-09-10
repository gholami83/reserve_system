from rest_framework import serializers
from rest_framework.fields import empty
from ..models import Room,RoomChoice


class RoomSerializer(serializers.ModelSerializer):
    choice_room_number = serializers.SerializerMethodField()
    def get_choice_room_number(self,instance):
        return instance.choice_room_number.room_number
    
    guest = serializers.SerializerMethodField()
    def get_guest(self,instance):
        return instance.guest.guest.username + " " + instance.guest.guest.email
    
    date_reserved = serializers.SerializerMethodField()
    def get_date_reserved(self,instance):
        return instance.date_reserved
    
    reserved = serializers.SerializerMethodField()
    def get_reserved(self,instance):
        return instance.reserved
    
    class Meta:
        model = Room
        fields = [
            'choice_room_number',
            'guest',
            'date_reserved',
            'reserved',
        ]
class RoomChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChoice
        fields = [
            'room_number',
        ]

class ReserveRoomSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        
        view = self.context.get("view")
        if view.action in [
            "list",
            "retrieve",
        ] :
            self.fields["choice_room_number"] = serializers.SerializerMethodField()
            self.fields["guest"] = serializers.SerializerMethodField()

    def get_choice_room_number(self,instance):
        return instance.choice_room_number.room_number
    
    def get_guest(self,instance):
        return instance.guest.guest.username+ " " + instance.guest.guest.email
    
    class Meta:
        model = Room
        fields = [
            'choice_room_number',
            'guest',
            'date_reserved',
            'reserved',
        ]