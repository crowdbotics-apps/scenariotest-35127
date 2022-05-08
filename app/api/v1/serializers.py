from rest_framework import serializers
from app.models import App,Plan

class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"