from django.db import models

# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=3)

class Region(models.Model):
    name = models.CharField(max_length=50)

class Weather(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    tmax = models.FloatField(null=True)
    tmin = models.FloatField(null=True)
    tmean = models.FloatField(null=True)
    sunshine = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    raindays1mm = models.FloatField(null=True)
    airfrost = models.FloatField(null=True)


