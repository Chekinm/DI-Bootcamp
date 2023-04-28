from django.db import models

# Create your models here.
class TestClass (models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)

