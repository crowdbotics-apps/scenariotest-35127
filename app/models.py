from django.conf import settings
from django.db import models
class App(models.Model):
    'Generated Model'
    description = models.TextField()
    owner = models.ForeignKey("users.User",null=True,blank=True,on_delete=models.CASCADE,related_name="app_owner",)
    name = models.CharField(null=True,blank=True,max_length=256,)
class Plan(models.Model):
    'Generated Model'
    name = models.CharField(max_length=256,)
    price = models.IntegerField(null=True,blank=True,)
class Subscription(models.Model):
    'Generated Model'
    app = models.ForeignKey("app.App",on_delete=models.CASCADE,related_name="subscription_app",)
    plan = models.ForeignKey("app.Plan",on_delete=models.CASCADE,null=True,blank=True,related_name="subscription_plan",)
    active = models.BooleanField(null=True,blank=True,)

# Create your models here.
