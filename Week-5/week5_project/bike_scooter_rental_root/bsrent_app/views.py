from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import  Customer, Station, Address
from .models import Rental, Vehicle
from .forms import CustomerForm, StationForm, VehicleForm, AddAddress 

############################### ADD FORMS ######################################

class AddVehicle(generic.CreateView):

    template_name = 'bsrent_app/add_vehicle.html'
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('all_vehicles')

class AddStation(generic.CreateView):

    template_name = 'bsrent_app/add_station.html'
    model = Station
    form_class = StationForm
    success_url = reverse_lazy('all_stations')

class AddAddress(generic.CreateView):

    template_name = 'bsrent_app/add_address.html'
    model = Address
    form_class = AddAddress
    success_url = reverse_lazy('manage_database')


class AddCustomer(generic.CreateView):

    template_name = 'bsrent_app/add_customer.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('all_customers')


################################ CUSTOMER ####################################

class AllCustomer(generic.ListView):
    
    template_name = 'bsrent_app/all_customers.html'
    context_object_name = 'customers'
    paginate_by = 20
    model = Customer

class OneCustomer (generic.DetailView):
    
    template_name = 'bsrent_app/one_customer.html'
    context_object_name = 'customer'
    model = Customer
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        rentals = customer.customer_rental.all()
        context['retnals_open'] = rentals.filter(return_date__isnull=True).order_by('start_date')
        context['rentals_closed'] = rentals.filter(return_date__isnull=False).order_by('start_date')
        return context
   

###################################### RENTALS  #####################################

def rentals (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/rentals.html', context)

class OpenRentals(generic.ListView):

    model = Rental
    template_name = 'bsrent_app/open_rentals.html'
    context_object_name = 'open_rentals'
    queryset = Rental.objects.all().filter(return_date__isnull=True).order_by('start_date')
    paginate_by = 15


class ClosedRentals(generic.ListView):

    model = Rental
    template_name = 'bsrent_app/closed_rentals.html'
    context_object_name = 'closed_rentals'
    queryset = Rental.objects.all().filter(return_date__isnull=False).order_by('start_date')
    paginate_by = 15
    
class OneRental(generic.DetailView):

    template_name = 'bsrent_app/one_rental.html'
    context_object_name = 'rental'
    model = Rental
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        rental = self.get_object()
        vehicle = rental.vehicle
        customer = rental.customer
        return_date = rental.return_date if rental.return_date !=None else 'Not returned yet'
        print(return_date)
        context.update(
                {'vehicle':vehicle,
                'customer':customer,
                'return_date':return_date
                }
                )
        return context


########################################### STATIONS #######################################

class AllStations(generic.ListView):

    model = Station
    template_name = 'bsrent_app/all_stations.html'
    context_object_name = 'all_stations'
    paginate_by = 15


class OneStation(generic.DetailView, generic.list.MultipleObjectMixin):

    template_name = 'bsrent_app/one_station.html'
    context_object_name = 'station'
    model = Station
    paginate_by = 10
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        station = self.get_object()
        station_records = station.vehicle_at_station
        vehicle_at_station = station_records.filter(departure_date__isnull=True).order_by('vehicle') 
        object_list = vehicle_at_station
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context
    
    # For more details on MiltipleObjectMixin to paginate secondary model 
    #  https://stackoverflow.com/questions/25569551/pagination-from-a-django-detailview


####################################### VEHICLE #################################

class AllVehicles(generic.ListView):

    model = Vehicle
    template_name = 'bsrent_app/all_vehicles.html'
    query_set = Vehicle.objects.all().order_by('id')
    context_object_name = 'all_vehicles'
    paginate_by = 10


class OneVehicle(generic.DetailView):

    template_name = 'bsrent_app/one_vehicle.html'
    context_object_name = 'vehicle'
    model = Vehicle
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        vehicle = self.get_object()
        vehicle_rentals = vehicle.vehicles_rentals
        context.update({
               'vehicle_rentals': vehicle_rentals,
               'status_msg':vehicle.status_string,
                })        
        return context


######################UPDATE VIEWS###########################

class StartRental(generic.UpdateView):
    model=Rental
    template_name = 'update_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")



class EndRental(generic.UpdateView):
    
    model=Rental
    
    
    pass



############################some test on post and get ##########################


def test(request):

    if request.method == 'GET':
        print(request.GET)

        context = {'form': 'test'
                   }

        return render(request, 'bsrent_app/test.html', context)


    elif request.method == 'POST':
        print(request.POST)
        post_content = request.POST
        context = {'form': 'test'
                   }

        return render(request, 'bsrent_app/test.html', context)

    



    

    

















