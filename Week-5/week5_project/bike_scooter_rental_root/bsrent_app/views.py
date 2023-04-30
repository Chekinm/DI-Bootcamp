from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import  Customer, Station, Address
from .models import VehicleType, VehicleSize, Vehicle, RentalRate
from .models import Rental, VehicleAtStation
from .forms import CustomerForm, StationForm, VehicleForm, StartRental, AddAddress 



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


##################### Main pages #################################
def rent (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/rent.html', context)

def manage_database (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/manage_database.html', context)

#################################################################


#################### customers ##################################

def all_customers (request, number_of_customer_per_page=20):
    """main customers page"""
    
    customers_list = Customer.objects.all().order_by('last_name')
    
    #copy from documetntaion 
    paginator = Paginator(customers_list, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # end of paginator 
    context = {"page_obj": page_obj}
    
    return render(request, 'bsrent_app/all_customers.html', context)


def one_customer (request, id:int):
    """detailed customer page"""
    customer = Customer.objects.get(pk=id)

    rentals = customer.customer_rental.all()
    retnals_open = rentals.filter(return_date__isnull=True).order_by('start_date')
    rentals_closed = rentals.filter(return_date__isnull=False).order_by('start_date')
    
    context = {'customer':customer,
               'retnals_open':retnals_open,
               'rentals_closed':rentals_closed
               }
    
    return render(request, 'bsrent_app/one_customer.html', context)


###################### rentals  --------------------------

def rentals (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/rentals.html', context)



def open_rentals (request, number_of_customer_per_page=10):
    """open retnals page"""
    
    open_rentals_list = Rental.objects.all().filter(return_date__isnull=True).order_by('start_date')
       
    paginator = Paginator(open_rentals_list, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {"page_obj": page_obj}
    
    return render(request, 'bsrent_app/open_rentals.html', context)


def closed_rentals (request, number_of_customer_per_page=10):
    """closed retnals page"""
        
    closed_rentals_list = Rental.objects.all().filter(return_date__isnull=False).order_by('start_date')
        
    paginator = Paginator(closed_rentals_list, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {"page_obj": page_obj}
    
    return render(request, 'bsrent_app/closed_rentals.html', context)


def one_rental (request, id:int):
    """detailed rentals page"""

    rental = Rental.objects.get(pk=id)
    vehicle = rental.vehicle
    customer = rental.customer

    return_date = rental.return_date if rental.return_date !=None else 'Not returned yet'


    context = {'rental':rental,
               'vehicle':vehicle,
               'customer':customer,
               'return_date':return_date
               }
    
    return render(request, 'bsrent_app/one_rental.html', context)







################## STATIONS #######################################


def all_stations (request, number_of_customer_per_page=10):
    """main station page"""
    
    stations_list = Station.objects.all()
    
    paginator = Paginator(stations_list, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # end of paginator 
    context = {"page_obj": page_obj}
    
    return render(request, 'bsrent_app/all_stations.html', context)


def one_station (request, id:int, number_of_customer_per_page=10):
    """detailed station page"""
    station = Station.objects.get(pk=id)

    station_records = station.vehicle_at_station
    vehicle_at_station = station_records.filter(departure_date__isnull=True).order_by('vehicle')
    

    paginator = Paginator(vehicle_at_station, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {'station':station,
               'page_obj':page_obj,
               }
    
    return render(request, 'bsrent_app/one_station.html', context)



########################## VEHICLE #################################

def all_vehicles (request, number_of_customer_per_page=10):
    """main vehicle page"""
    
    vehicles_list = Vehicle.objects.all().order_by('id')
    
    paginator = Paginator(vehicles_list, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    context = {'page_obj': page_obj,
                }
    
    return render(request, 'bsrent_app/all_vehicles.html', context)


def one_vehicle (request, id:int):
    """detailed vehicle page"""

    vehicle = Vehicle.objects.get(pk=id)
    vehicle_rentals = vehicle.vehicles_rentals

    if vehicle.status == 2:
        status_msg = f'''Vehicle is is not at the staion yet'''
    elif vehicle.status == 0:
        vehicle_rentals = vehicle.vehicles_rentals.order_by('-start_date')[0]
        last_renter = vehicle_rentals.customer 
        vehicles_stations = vehicle.vehicles_station_record.order_by('-arrival_date')[0]
        last_station = vehicles_stations.station.name
        status_msg = f'''Vehicle is currently rented by {last_renter}\n
        It was rented on {vehicle_rentals.start_date}, at the {last_station} rental station.'''
    else:
        vehicles_stations = vehicle.vehicles_station_record.order_by('-arrival_date')[0]
        last_station = vehicles_stations.station.name
        status_msg = f'''Vehicle is currently availble for rent  at {last_station} rental station.'''



    context = {'vehicle': vehicle,
               'vehicle_rentals': vehicle_rentals,
               'status_msg':status_msg,
               }
    
    return render(request, 'bsrent_app/one_vehicle.html', context)




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

        
        
        #print(customer_filled_form.cleaned_data)
        
        # if request.POST.get("form_type") == 'customer':
        #     customer_filled_form = CustomerForm(request.POST) # put the data from the request into the ModelForm

        #     if customer_filled_form.is_valid(): # check if all fields contain the correct data
        #         print(customer_filled_form.cleaned_data)
        #         # customer_filled_form.save() # save data into database
        #         return HttpResponse("SUCCESSFULLY SAVED")


   
        # elif request.POST.get("form_type") == 'address':
        #     address_filled_form = AddAddress(request.POST) # put the data from the request into the ModelForm

        #     if address_filled_form.is_valid(): # check if all fields contain the correct data
        #         print(address_filled_form.cleaned_data)
        #         # address_filled_form.save() # save data into database
        #         return HttpResponse("SUCCESSFULLY SAVED")




    

    

















