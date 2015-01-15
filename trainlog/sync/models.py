from django.db import models
from django.contrib.auth.models import User

class Idonethis(models.Model):
    user = models.ForeignKey(User)
    api_key = models.CharField(max_length=100)

class Strava(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
