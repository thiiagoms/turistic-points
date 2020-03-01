from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Comments(models.Model):
    """ Classe de comentários que um usuário pode fazer """
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_comment.first_name