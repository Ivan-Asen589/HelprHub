"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('login/', views.login, name='login'), # Added /
    
    path('signup/', views.signup, name='signup'), 

    path('nujdaeshti/', views.nujdaeshti, name='nujdaeshti'),
    path('pomagashti/', views.pomagashti, name='pomagashti'),
    path('posts/', include('posts.urls')),
    path('helper_selector/', views.nujdaeshti, name='helper_selector'),
]
=======
    path('login', views.login, name='login'),
    path('nujdaeshti', views.nujdaeshti, name='nujdaeshti'),
    path('pomagashti', views.pomagashti, name='pomagashti'),
    path('posts/', include('posts.urls')),
    path('helper_selector', views.nujdaeshti, name='helper_selector'),
    path('profil_potrebitel', views.profil_potrebitel, name='profil_potrebitel'),
    
    ]
>>>>>>> 8d8ef3ce3023db157ad63bcaaface84fb3583d85
