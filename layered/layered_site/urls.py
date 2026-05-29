from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", views.login_view, name="login"),
    path("auth/logout/", views.logout_view, name="logout"),
    path("oauth/callback/", views.auth_callback, name="auth_callback"),
    path("dashboard/", views.dashboard, name="dashboard"),
]   