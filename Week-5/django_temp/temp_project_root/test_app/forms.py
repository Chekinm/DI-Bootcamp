from django.forms import ModelForm
from .models import TestClass
from  django.forms import forms

class TestForm(ModelForm):
    class Meta:
        model = Gif 
        fields = '__all__'
        
