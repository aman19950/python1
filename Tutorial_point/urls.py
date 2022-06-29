from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("contact", views.contact_dtls, name="con"),
    path("registration", views.sign_up, name="signup"),
    path("login", views.login, name="login"),

]
