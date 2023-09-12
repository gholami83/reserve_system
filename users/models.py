from datetime import date,timedelta
from django.utils import timezone
from django.db import models 
from django.utils.timezone import now
from django.contrib.auth import get_user_model


def get_date_time():
    return date.today() + timedelta(days=3)


class Room(models.Model):
    reserver_name = models.CharField(max_length=50,null=False)
    room_number = models.IntegerField(default=0,blank=False)
    date_reserve = models.DateField(default = date.today(),null=True)
    reserved = models.BooleanField(default=False)
    date_unreserved = models.DateField(default= get_date_time,null=True)

    def __str__(self) -> str:
        return str(self.room_number + self.reserved)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.BigIntegerField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)


class Admin(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True)

