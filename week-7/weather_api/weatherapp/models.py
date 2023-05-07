from django.db import models

# Create your models here.

TYPE_CHOICES = (

    ('sunny', 'Sunny'),
    ('cloudy','Storm'),
    ('windy','Sunny'), 
    ('rainy','Rainy'),
    ('stormy','Stormy'),
)


class Report(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    weather_type = models.CharField(max_length=8, choices=TYPE_CHOICES, null=True)
