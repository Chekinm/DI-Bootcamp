from django.shortcuts import render
from django.core.paginator import Paginator
from .models import TestModel, Customer, Station, Address
from .models import VehicleType, VehicleSize, Vehicle, RentalRate
from .models import Rental, VehicleAtStation
from .forms import TestForm, CustomerForm



##################### Main page #################################
def rent (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/rent.html', context)

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
    status_list = [vehicle.vehicles_station_record.order_by('-arrival_date')[0].departure_date for vehicle in vehicles_list]
    
    # this is very slow and memory abusing method, but
    # I don't fian another way to find current status of vehicle
    # actially, we don't need it here.
    vehicles_list_plust_status = list(zip(vehicles_list,status_list))

    paginator = Paginator(vehicles_list_plust_status, number_of_customer_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   

    context = {'page_obj': page_obj,
                }
    
    return render(request, 'bsrent_app/all_vehicles.html', context)


def one_vehicle (request, id:int):
    """detailed vehicle page"""

    vehicle = Vehicle.objects.get(pk=id)

    vehicle_rentals = vehicle.vehicles_rentals.order_by('-start_date')[0]
    last_renter = vehicle_rentals.customer 
    
    vehicles_stations = vehicle.vehicles_station_record.order_by('-arrival_date')[0]
    last_station = vehicles_stations.station.name

    
    if vehicle_rentals.return_date == None:
        status_msg = f'''Vehicle is currently rented by {last_renter}</a>\n
        It was rented on {vehicle_rentals.start_date}, at the {last_station} rental station.'''
    elif vehicles_stations.departure_date != None:
        status_msg = f'''Vehicle is currently on repair.\n
        Last station was {last_station} rental station.'''
    else:
        status_msg = f'''Vehicle is currently availble for rent  at {last_station} rental station.'''


    
    context = {'vehicle': vehicle,
               'vehicle_rentals': vehicle_rentals,
               'vehicles_stations':vehicles_stations,
               'last_renter': last_renter,
               'last_station': last_station,
               'status_msg':status_msg,
               }
    
    return render(request, 'bsrent_app/one_vehicle.html', context)




















def add_user (request):
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form_content':form}

    if request.method == 'GET':
       
        form = CustomerForm()
        print(form)
        context = {'form_content':form}

    
    return render(request, 'bsrent_app/add_user.html', context)





# /rent/rental/ - show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)




# /rent/rental/<pk> - show the information about the given rental:
# customer details
# vehicle details
# rental details (“Returned on: <date>” / “Not yet returned”)

# click on a rental and be taken to the page to view that rental.



# /rent/rental/add – provide a form to enter a customer ID and a vehicle ID to create a rental.
# If the customer or the vehicle does not exist, show a user-friendly error message.
# If the vehicle is currently being rented, show a relevant error message.

# Add a rental – form with dropdowns to select a customer and a vehicle. (We’ll hopefully improve on this design at a later stage). Do not include vehicles which are currently being rented!

# click on customer to go to customer page; click on vehicle to go to vehicle page; click a button BACK TOvehicle to return the rental.


# /rent/customer/<pk> - show the customer matching the given ID


# /rent/customer/ - show all customers, in alphabetical order



# /rent/customer/add – provide a form to add a new customer






# /rent/vehicles/group
# /rent/vehicles/group/small
# /rent/vehicles/group/medim
# /rent/vehicles/group/big


# /rent/station/add – create a new station


# rent/station/<station_id> - show information about the station. Include a list of all vehicles currently at the station.

# rent/station/distribution – show information about all stations. For each station, display:
# how many vehicles are currently at the station
# of each type
# include percentages of the whole, eg. if 73% are bikes, show “Bike – 73%”“.
# Percentages and information about how busy each station is, relative to the other stations (use percentages).


# /rent/vehicle/<pk> - show the specific vehicle
# also show whether it’s currently being rented

# /rent/vehicle/add – provide a form to add a new vehicle.

# /rent/station – show all stations

