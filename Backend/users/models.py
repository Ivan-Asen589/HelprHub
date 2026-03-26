from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    town = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
