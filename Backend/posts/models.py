import datetime
from django.db import models

class Post(models.Model):
    publisher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    locationTown = models.CharField(max_length=30)
    locationNeighborhood = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    date = models.DateField(default=datetime.datetime.now)
    time = models.TimeField(default=datetime.time.min)