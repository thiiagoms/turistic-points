from django.db import models
from attractions.models import Attractions
from locations.models import Locations
from comments.models import Comments
from reviews.models import Reviews


# Create your models here.
class TuristicPoints(models.Model):
    """ Classe de pontos turísticos e seus respectivos relacionamentos"""
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comments = models.ManyToManyField(Comments)
    reviews = models.ManyToManyField(Reviews)
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name