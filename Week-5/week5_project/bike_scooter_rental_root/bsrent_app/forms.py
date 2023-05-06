from django import forms
from bsrent_app.models import  Address, Customer, Station, RentalRate, Rental
from bsrent_app.models import  VehicleAtStation, VehicleType, VehicleSize, Vehicle


class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = Vehicle
        fields = '__all__'
        exclude = ["status"]




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

 
class StationForm(forms.ModelForm):
    
    class Meta:
        model = Station
        fields = '__all__'


class AddAddress(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'

    


class StartRental(forms.ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'


