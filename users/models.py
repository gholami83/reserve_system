from datetime import date,timedelta
from django.db import models 
from django.contrib.auth import get_user_model


def get_date_time():
    return date.today() + timedelta(days=3)


class Room(models.Model):
    room_number = models.IntegerField(default=0)
    date_reserve = models.DateField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    date_unreserved = models.DateField(default= get_date_time)
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

