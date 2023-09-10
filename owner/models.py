from django.contrib.auth import get_user_model
from django.db import models
from guests.models import Guest
from rooms.models import Room


class Owner(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE,null=True)
    
