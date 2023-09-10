from rest_framework.fields import empty
from rest_framework import serializers
from ..models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'room',
            'guest',
        ]

    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)

        view = self.context.get("view")
        if view.action in [
            'list',
            'retrieve',
        ]:
            self.fields["room"] = serializers.SerializerMethodField()
            self.fields["guest"] = serializers.SerializerMethodField()

    def get_room(self,instance):
        return {
            "room_number" : instance.room.choice_room_number.room_number,
            "date_reserved" : instance.room.date_reserved,
            "reserved": instance.room.reserved
            }
    
    def get_guest(self,instance):
        return {
            "username" : instance.guest.guest.username,
            "email" : instance.guest.guest.email
            }
    
