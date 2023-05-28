from django.db import models

# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=3)

class Region(models.Model):
    name = models.CharField(max_length=50)

class Weather(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    tmax = models.FloatField()
    tmin = models.FloatField()
    tmean = models.FloatField()
    sunshine = models.FloatField()
    rainfall = models.FloatField()
    raindays1mm = models.FloatField()
    airfrost = models.FloatField()


