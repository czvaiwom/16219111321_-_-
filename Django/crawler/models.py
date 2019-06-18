from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=10000)
    synopsis = models.CharField(max_length=10000)
    time = models.CharField(max_length=200)

class Weathers(models.Model):
    city = models.CharField(max_length=200)
    dates = models.CharField(max_length=200)
    winL = models.CharField(max_length=200)
    temperatureLow = models.CharField(max_length=200)
    temperatureHigh = models.CharField(max_length=200)
    weather = models.CharField(max_length=20)

class Phones(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=10000)
    price=models.CharField(max_length=200)
    time = models.CharField(max_length=200)