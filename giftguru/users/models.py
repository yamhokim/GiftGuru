from django.db import models

# Create your models here.
class CustomUser(models.Model):
    preferences = models.TextField(blank=True, null=True)
    