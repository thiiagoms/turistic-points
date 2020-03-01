from django.db import models


# Create your models here.
class Locations(models.Model):
    """ Localizações de um ponto turistico """
    row = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    latitude = models.FloatField(max_length=150)
    longitude = models.FloatField(max_length=150)

    def __str__(self):
        return self.row
