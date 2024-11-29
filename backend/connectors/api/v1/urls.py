from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137612ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137612", Testconnectors137612ViewSet, basename="testconnectors137612"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
