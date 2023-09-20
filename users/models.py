from datetime import date,timedelta
from django.utils import timezone
from django.db import models 
from django.utils.timezone import now
from django.contrib.auth import get_user_model


def get_date_time():
    return date.today() + timedelta(days=3)

class Hotel(models.Model):
    name = models.CharField(max_length=50,unique=True)
    address = models.TextField()
    phone = models.BigIntegerField()
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    reserver_name = models.CharField(max_length=50,null=False)
    room_number = models.IntegerField(blank=False)
    until_reserve = models.DateTimeField(null=True)
    
    def __str__(self) -> str:
        return str(self.room_number)


