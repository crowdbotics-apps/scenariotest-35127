from rest_framework import authentication
from app.models import App,Plan
from .serializers import AppSerializer,PlanSerializer
from rest_framework import viewsets

class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = App.objects.all()

class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Plan.objects.all()