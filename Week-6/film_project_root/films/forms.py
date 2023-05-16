from django import forms
from .models import Country, Category, Director, Film

class FilmForm(forms.ModelForm):
   
    class Meta:
        model=Film
        fields = ('__all__')
    
    

class DirectorForm(forms.ModelForm):
    
    class Meta:
        model=Director
        fields = ('__all__')

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category 
        fields = ('__all__')

class CountryForm(forms.ModelForm):
    
    class Meta:
        model = Country
        fields = ('__all__')



    

    
   