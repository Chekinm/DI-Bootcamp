from django.db import models
from accounts.models import UserProfile
from datetime import date
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    author = models.ForeignKey(UserProfile,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    date_created = models.DateField(null=True, validators=[MinValueValidator(date.today()), MaxValueValidator(date.today())])

    def __str__(self) -> str:
        return self.title