from django.db import models

# Create your models here.
class Information(models.Model):
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    no = models.CharField(max_length=200)
