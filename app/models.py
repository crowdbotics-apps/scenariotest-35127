from django.conf import settings
from django.db import models
class App(models.Model):
    'Generated Model'
    name = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True,related_name="app_owner",)

# Create your models here.
