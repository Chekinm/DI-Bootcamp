from django import forms
from .models import Category, ToDoTask


class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = ToDoTask
        fields = '__all__'
        
        