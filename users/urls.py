from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', login_user),
    path('logout/', logout_user),
    path('register/', register_user)
]
