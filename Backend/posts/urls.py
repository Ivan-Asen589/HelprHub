from django.urls import path
from . import views
from .views import PostCreateView

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('', PostCreateView.as_view(), name='postcreateview'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post'),
    path('<int:pk>/volunteer/', views.volunteer_signup, name='volunteer_signup'),
    path('<int:pk>/optout/', views.volunteer_optout, name='volunteer_optout'),
]
