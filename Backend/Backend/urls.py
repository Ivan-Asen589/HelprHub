from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from users.views import SignUp, LogIn, LogOut, UserDeleteView, profile
from posts.views import PostCreateView, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', LogIn, name='login'),
    path('logout/', LogOut, name='logout'),
    path('signup/', SignUp, name='signup'),
    path('nujdaeshti/', PostCreateView.as_view(), name='nujdaeshti'),
    path('pomagashti/', views.pomagashti, name='pomagashti'),
    path('helper_selector/', PostListView.as_view(), name='helper_selector'),
    path('posts/', include('posts.urls')),
    path('profile/', profile, name='profile'),
    path('profiles/', profile),
    path('profile/delete/', UserDeleteView.as_view(), name='delete_account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
