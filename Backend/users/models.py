from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    #username = models.CharField(max_length=30)
    #password = models.CharField(max_length=30)
    phone_number = PhoneNumberField()
    town = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)


