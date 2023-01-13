from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post'),
    path('profile/<str:username>/',views.profile, name='profile'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)