from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.post, name='post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)