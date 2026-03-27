from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField(blank=True)
    town = models.CharField(max_length=30, blank=True)
    neighborhood = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    USER_TYPE_CHOICES = [
        ('helper', 'Helper'),
        ('receiver', 'Receiver'),
    ]
    user_role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='helper')

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(max_length=1000)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    locationTown = models.CharField(max_length=100)
    locationNeighborhood = models.CharField(max_length=200)
    
    volunteer = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='users_volunteered_posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.description[:20]}"