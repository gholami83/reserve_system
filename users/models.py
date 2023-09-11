from datetime import date,timedelta
from django.db import models 
def get_date_time():
    return date.today() + timedelta(days=3)


class Hotel(models.Model):
    room_number = models.IntegerField(default=0)
    date_reserved = models.DateField(auto_now_add=True)
    resrved = models.BooleanField(default=False)
    date_unreserved = models.DateField(default= get_date_time)


class Admin(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,null=True)

