from django.contrib import admin
from django.urls import path
from core.views import index
from django.contrib.auth import views as auth_views
from core.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("profile/", profile_view, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
