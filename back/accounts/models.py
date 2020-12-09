from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followings')
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.username