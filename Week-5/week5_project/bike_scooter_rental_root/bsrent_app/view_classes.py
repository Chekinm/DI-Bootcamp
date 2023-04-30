from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import TestModel, Customer, Station, Address
from .models import VehicleType, VehicleSize, Vehicle, RentalRate
from .models import Rental, VehicleAtStation
from .forms import CustomerForm, StationForm, VehicleForm, StartRental, AddAddress

class AddVehicle(generic.CreateView):

    template_name = 'bsrent_app/add_vehicle.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('all_vehicles')

 