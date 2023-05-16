from django.db import models
from datetime import date

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.second_name}'

class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(default=date.today)
    created_in_country = models.ForeignKey(Country, 
                                           on_delete=models.SET_NULL,
                                           blank=True, 
                                           null=True,
                                           related_name='films_created_in_country')
    available_in_countries = models.ManyToManyField(Country, 
                                                    related_name='films_avialable_in_country')
    category = models.ManyToManyField(Category, related_name='films')
    director = models.ManyToManyField(Director, related_name='films')

    def __str__(self):
        return f'{self.title}'
    

