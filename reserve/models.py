from django.db import models
from rooms.models import Room
from owner.models import Owner


class Reserve(models.Model):
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)
