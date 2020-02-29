from django.db import models

# Create your models here.
class Attractions(models.Model):
    """ Atrações dos pontos turisticos """
    name = models.CharField(max_length=150)
    description = models.TextField()
    open_hour = models.TimeField()
    close_hour = models.TimeField()
    age = models.IntegerField()
    attr_img = models.ImageField(upload_to='img_attractions', null=True, blank=True)

    
    def __str__(self):
        return self.name