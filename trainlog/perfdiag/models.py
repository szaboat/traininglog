from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    created = models.DateField()
    user = models.ForeignKey(User)
    height = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    fat = models.IntegerField()
    fat_subscapular = models.IntegerField()
    fat_trizeps = models.IntegerField()
    fat_bizeps = models.IntegerField()
    fat_suprailiacal = models.IntegerField()
    bmi_index = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    rest_pulse = models.IntegerField()
    rest_blood_pressure_systolic = models.IntegerField()
    rest_blood_pressure_diastolic = models.IntegerField()
    rest_lactate = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    rest_hemoglobin = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    rest_hematocryt = models.IntegerField()
    rest_bloodsugar = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    r1_pulse = models.IntegerField()
    r3_pulse = models.IntegerField()
    r5_pulse = models.IntegerField()

    r5_rest_blood_pressure_systolic = models.IntegerField()
    r5_rest_blood_pressure_diastolic = models.IntegerField()

    regeneration_quotient = models.DecimalField(max_digits=4, decimal_places=2, null=True)
