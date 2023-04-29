from django.shortcuts import render
from .models import TestModel, Customer
from .forms import TestForm, CustomerForm

def rent (request):
    """main page, nothing to automate, see corresponding html"""
    context = {}
    return render(request, 'bsrent_app/rent.html', context)


def all_customers (request, number_of_customer_per_page=10):
    """main customers page"""
    customers_list = Customer.objects.all()[:number_of_customer_per_page]

    context = {'customers_list':customers_list}
    
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



def index (request):
    test = Customer.objects.all()
    print(test[0])
    context = {'content':test[0],
               'greeting':'Hello'}
    
    return render(request, 'bsrent_app/index.html', context)





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

