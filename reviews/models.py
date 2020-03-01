from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Reviews(models.Model):
    """ Note for the comments """
    user_review = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    description = models.DecimalField(max_digits=4, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_review.first_name
