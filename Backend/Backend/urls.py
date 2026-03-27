from django.contrib import admin
from django.urls import path, include
from . import views
from posts.views import PostCreateView, PostListView
from users.views import SignUp, LogIn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', LogIn, name='login'),
    path('signup/', SignUp, name='signup'),
    path('nujdaeshti/', PostCreateView.as_view(), name='nujdaeshti'),
    path('pomagashti/', views.pomagashti, name='pomagashti'),
    path('helper_selector/', PostListView.as_view(), name='helper_selector'),
    path('posts/', include('posts.urls')),
    path('profile/', views.profile, name='profile'),
]