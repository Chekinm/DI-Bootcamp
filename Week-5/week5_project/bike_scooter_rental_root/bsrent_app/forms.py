from django import forms
from .models import TestModel, Customer




class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'




class CustomerForm(forms.Form):
  class Meta:
        model = Customer
        fields = '__all__'
        