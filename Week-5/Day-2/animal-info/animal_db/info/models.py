from django.db import models

class Family (models.Model):
    # id automaticly created
    name = models.CharField(max_length=50)  # varchar in SQL

class Animal (models.Model):

    name = models.CharField(max_length=50)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField(null=True)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    imageurl = models.CharField(max_length=250, blank=True,  null=True)
