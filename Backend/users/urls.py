from django.urls import path
from . import views
from . import LogIn
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', LogIn, name='login'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
    path('profile/delete/', views.UserDeleteView.as_view(), name='delete_account'),
    path('contact/', views.contact_us, name='contact_us'),
]
