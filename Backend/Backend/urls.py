from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
<<<<<<< HEAD

    path('nujdaeshti', views.nujdaeshti, name='nujdaeshti'),
    path('pomagashti', views.pomagashti, name='pomagashti'),
    path('posts/', include('posts.urls')),
    path('helper_selector', views.nujdaeshti, name='helper_selector'),

=======
>>>>>>> 1d48bb18fa95d5bd015abd19d9b5c9ab9e59d3f4
]
