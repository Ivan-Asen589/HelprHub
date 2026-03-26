from django.db import models

# Create your models here.
class Post(models.Model):
    publisher = models.ForeignKey('users.User', on_delete=models.CASCADE)
    heading = models.CharField(max_length=30)
    locationTown = models.CharField(max_length=30)
    locationNeighborhood = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)