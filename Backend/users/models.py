from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField(blank=True)
    town = models.CharField(max_length=30, blank=True)
    neighborhood = models.CharField(max_length=30, blank=True)
    USER_TYPE_CHOICES = [
        ('helper', 'Helper'),
        ('receiver', 'Receiver'),
    ]
    type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='helper')