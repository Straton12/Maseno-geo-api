from django.contrib.gis.db import models

# Create your models here.
class MyModel(models.Model):
    fid_field = models.FloatField()
    name = models.CharField(max_length=254)
    structure = models.CharField(max_length=254)
    use = models.CharField(max_length=254)
    no_floors = models.FloatField()
    rooms = models.FloatField()
    capacity = models.CharField(max_length=254)
    stracture = models.CharField(max_length=254)
    x = models.FloatField()
    y = models.FloatField()
    geom = models.PointField(srid=4326)
