from django.db import models

# Create your models here.

from django.db import models

class AyurvedicPrediction(models.Model):
    cold = models.IntegerField()
    eyepain = models.IntegerField()
    fever = models.IntegerField()
    headache = models.IntegerField()
    stomachache = models.IntegerField()
    dizziness = models.IntegerField()
    vomiting = models.IntegerField()
    chestpain = models.IntegerField()
    jointpain = models.IntegerField()
    loosemotion = models.IntegerField()
    throatinfection = models.IntegerField()
    age = models.IntegerField()
    gender = models.IntegerField()
    weight = models.IntegerField()
    medicine1 = models.CharField(max_length=100)
    medicine2 = models.CharField(max_length=100)
    medicine3 = models.CharField(max_length=100)

