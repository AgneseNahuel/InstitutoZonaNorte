from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),
    path("", views.inicio, name="inicio"),
    path("login/", LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("", include("VentaPost.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
