from django.db import models

# Create your models here.
class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    category = models.CharField(max_length=255)

class Recommendation(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    date_recommended = models.DateTimeField(auto_now_add=True)