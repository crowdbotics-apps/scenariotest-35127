
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AppViewSet,PlanViewSet,SubscriptionViewSet
router = DefaultRouter()
router.register('app', AppViewSet )
router.register('plan', PlanViewSet )
router.register('subscription', SubscriptionViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
