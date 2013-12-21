from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    name = models.CharField(max_length=255)
    resting_heart_rate = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    sleep_hours = models.IntegerField()
    sleep_quality = models.IntegerField() # TODO choice
    overall_mood = models.IntegerField() # TODO choice
    overall_mood_during_workout = models.IntegerField() # TODO choice
    strava_link = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created = models.DateField(auto_now=True)

    user = models.ForeignKey(User)
