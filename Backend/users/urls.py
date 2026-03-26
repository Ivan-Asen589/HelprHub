from django.urls import path
from . import views
from . import LogIn

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', LogIn, name='login'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
]
