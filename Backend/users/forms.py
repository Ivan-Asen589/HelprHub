from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # This adds the 'type' field so the OperationalError goes away
        fields = UserCreationForm.Meta.fields + ('user_role', 'town', 'phone_number')