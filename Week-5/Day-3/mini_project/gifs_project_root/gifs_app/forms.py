from django.forms import ModelForm
from .models import Gif, Category
from  django.forms import forms
class GifForm(ModelForm):
    class Meta:
        model = Gif 
        fields = '__all__'
        

        




