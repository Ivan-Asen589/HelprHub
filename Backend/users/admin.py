from django.contrib import admin
from .models import User

# This tells the admin panel to show the User table
admin.site.register(User)