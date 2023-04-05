# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("", views.home, name="home"),
    path("connect/", views.connect, name="connect"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path("create_event", views.create_event, name="create_event"),
    path("change_crops", views.change_crops, name="change_crops"),
    path("add_comment", views.add_comment, name="add_comment"),
]