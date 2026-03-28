from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField(blank=True)
    town = models.CharField(max_length=30, blank=True)
    neighborhood = models.CharField(max_length=70, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    USER_TYPE_CHOICES = [
        ('helper', 'Helper'),
        ('receiver', 'Receiver'),
    ]
    user_role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='helper')