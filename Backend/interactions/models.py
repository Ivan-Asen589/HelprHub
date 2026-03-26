from django.db import models

# Create your models here.
class Request(models.Model):
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    heading = models.CharField(max_length=30)


