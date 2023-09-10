from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UsersSerializer(ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'email',
        ]