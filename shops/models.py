from django.contrib.gis.db import models

class Shop(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    location = models.PointField() #represents a pair of longitude and latitude coordinates.
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

