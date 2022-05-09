from rest_framework import serializers
from app.models import App,Plan,Subscription

class AppSerializer(serializers.ModelSerializer):

    class Meta:
        model = App
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = "__all__"

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"