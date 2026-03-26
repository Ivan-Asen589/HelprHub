from django.contrib import admin
from django.urls import path, include
from . import views
from posts.views import PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'), # Your change
    path('nujdaeshti/', PostCreateView.as_view(), name='nujdaeshti'),
    path('pomagashti/', views.pomagashti, name='pomagashti'),
    path('posts/', include('posts.urls')),
    path('profile/', views.profile, name='profile'),
]