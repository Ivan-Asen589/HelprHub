from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from users.views import SignUp, LogIn, LogOut, UserDeleteView
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
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profile),
    path('profile/delete/', UserDeleteView.as_view(), name='delete_account'),
    path('403/', views.error_403, name='error_403'),
    path('404/', views.error_404, name='error_404'),
]

handler403 = 'Backend.views.error_403'
handler404 = 'Backend.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
