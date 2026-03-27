from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from users.views import SignUp, LogIn, LogOut, delete_account, contact_us
from posts.views import PostCreateView, PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', LogIn, name='login'),
    path('logout/', LogOut, name='logout'),
    path('signup/', SignUp, name='signup'),
    path('receivers/', PostCreateView.as_view(), name='receivers'),
    path('helpers/', views.helpers, name='helpers'),
    path('helper_selector/', PostListView.as_view(), name='helper_selector'),
    path('posts/', include('posts.urls')),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profile),
    path('delete_account/', delete_account, name='delete_account'),
    path('contact/', contact_us, name='contact_us'),
    path('403/', views.error_403, name='error_403'),
    path('404/', views.error_404, name='error_404'),
]

handler403 = 'Backend.views.error_403'
handler404 = 'Backend.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
