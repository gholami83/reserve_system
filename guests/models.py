from django.db import models
from django.contrib.auth import get_user_model


class Guest(models.Model):
    guest = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return str(self.guest)