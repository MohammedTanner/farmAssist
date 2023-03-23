# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.home, name="home"),
    path("connect/", views.ConnectPageView.as_view(), name="connect"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
]