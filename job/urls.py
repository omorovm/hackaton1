from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()

router.register('', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
