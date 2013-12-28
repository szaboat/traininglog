from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=255)
    created = models.DateField()
    skipped = models.BooleanField()

    TYPE = (
        ('W', 'Workout'),
        ('R', 'Rest'),
    )
    entry_type = models.CharField(max_length=1, choices=TYPE)

    sleep_hours = models.IntegerField()

    QUALITY = (
        (5, 'Excelent'),
        (4, 'Good'),
        (3, 'Medium'),
        (2, 'Poor'),
        (1, 'Bad'),
    )
    sleep_quality = models.IntegerField(choices=QUALITY) # TODO choice
    resting_heart_rate = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=1)

    strava_link = models.CharField(max_length=255, blank=True)
    hr_avg = models.IntegerField(blank=True, null=True)
    hr_max = models.IntegerField(blank=True, null=True)
    ga1 = models.IntegerField(blank=True, null=True) # seconds
    ga2 = models.IntegerField(blank=True, null=True) # seconds
    ga2_plus = models.IntegerField(blank=True, null=True) # seconds
    cal = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True) # seconds
    length = models.IntegerField(blank=True, null=True) # kms
    cadence_avg = models.IntegerField(blank=True, null=True)
    cadence_max = models.IntegerField(blank=True, null=True)
    speed_avg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    speed_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    mood = models.IntegerField(choices=QUALITY) # TODO choice
    mood_during_workout = models.IntegerField(choices=QUALITY, blank=True, null=True) # TODO choice

    description = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.name, self.user)
