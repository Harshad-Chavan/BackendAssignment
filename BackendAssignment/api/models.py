from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=8, blank=False, null=False)
    email = models.EmailField()
    followers = models.IntegerField()
    following = models.IntegerField


class Post(models.Model):
    user_id = models.IntegerField(default=1)
    description = models.TextField(max_length=200, blank=False, default="")
