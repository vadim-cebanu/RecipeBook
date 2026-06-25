from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloViewSet

router = DefaultRouter()
router.register(r'hello', HelloViewSet, basename='hello')

urlpatterns = [
    path('', include(router.urls)),
]
