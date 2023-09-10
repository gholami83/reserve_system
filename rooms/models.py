from django.db import models
from guests.models import Guest
from django.utils import timezone


class RoomChoice(models.Model):
    room_number = models.IntegerField(unique=True,null=True)
    def __str__(self):
        return str(self.room_number)


class Room(models.Model):
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    choice_room_number = models.ForeignKey(RoomChoice,on_delete=models.CASCADE)
    date_reserved = models.DateField(default=timezone.now)
    reserved = models.BooleanField(default=False)
    def __str__(self):
        return str(self.choice_room_number)             