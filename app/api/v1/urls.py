
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AppViewSet,PlanViewSet
router = DefaultRouter()
router.register('app', AppViewSet )
router.register('plan', PlanViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
