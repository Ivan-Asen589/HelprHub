from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),

    path('nujdaeshti', views.nujdaeshti, name='nujdaeshti'),
    path('pomagashti', views.pomagashti, name='pomagashti'),
    path('posts/', include('posts.urls')),
    path('helper_selector', views.nujdaeshti, name='helper_selector'),

]
