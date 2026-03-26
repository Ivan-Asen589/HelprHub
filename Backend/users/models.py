from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = PhoneNumberField()
    town = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=30)
    
    # ADD THIS LINE BELOW:
    user_role = models.CharField(max_length=20, null=True, blank=True)