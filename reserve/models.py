from django.db import models
from rooms.models import Room
from owner.models import Owner
from guests.models import Guest


class Reserve(models.Model):
    owner = models.ForeignKey(Guest,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)
