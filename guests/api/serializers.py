from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Guest


class GuestSerializer(ModelSerializer):
    def get_guest(self,instance):
        return instance.guest.username+ "-" + instance.guest.email
    
    def __init__(self, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        view = self.context.get('view')
        if view.action in [
            'list',
            'retrive',
        ] :
            self.fields['guest'] = serializers.SerializerMethodField()
    
    class Meta:
        model = Guest
        fields = [
            'guest',
        ]