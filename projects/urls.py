from django.contrib import admin
from django.urls import path, include

from .models import Message
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('message', MessageViewset)
router.register('tag', TagViewSet)
router.register('review', ReviewViewSet)
router.register('skill', SkillViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # path('projects/', Projects.as_view()),
    # path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
