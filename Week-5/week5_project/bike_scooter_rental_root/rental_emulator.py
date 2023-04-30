import os
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_scooter_rental.settings')
django.setup()
from bsrent_app.models import  Address, Customer, Station, RentalRate, Rental, VehicleAtStation, VehicleType, VehicleSize, Vehicle
import datetime
from random import sample, randint, choice


START_DATE = datetime.date(2018, 1, 1)
DATE_ITER = datetime.timedelta(2)
current_date = datetime.date(2018, 1, 1)
NUMBER_OF_CUSTOMER = 1000
NUMBER_OF_STATION = 10
NUMBER_OF_VEHICLE = 300


NUMBER_OF_DAYS = 300
MIN_RENT_PER_DAY = 5
MAX_RENT_PER_DAY = 10


def start_rental(customer, station, current_date):
    free_vehicle_list = VehicleAtStation.objects.filter(departure_date__isnull=True, station=station.id)
    if free_vehicle_list:
        free_vehicle_list[0].departure_date = current_date
        vehicle = free_vehicle_list[0].vehicle
        rental = Rental( 
                start_date   = current_date,
                # return_date  empry, means vehicl is on ride now
                customer     = customer,
                vehicle      = vehicle,
                )
        vehicle.status = 0
        vehicle.save()
        free_vehicle_list[0].save() # vehicle_at_station object
        rental.save()
    else:
        raise ValueError('Station is runing out of vehicle. Come back later, or choose another station')


def end_rental(rental, station):
    
    if rental.return_date == None:
        rental.return_date = current_date  # stop rental 
        vehicle = rental.vehicle
        # return vehicel to the rent station
        new_vehicle_at_station = VehicleAtStation(
                arrival_date    = current_date,
                # departure_date is empty means vehicl is free to rent
                vehicle         = vehicle,
                station         = station,
                     )
        vehicle.status = 1
        vehicle.save()
        rental.save()
        #print(rental.return_date)
        new_vehicle_at_station.save()
    else:
        raise ValueError('This rental is not open. Cannot be clsoed')

    


# start two rental manually, so that somethign can be clsoed in the cycle below
customer = Customer.objects.get(pk=1)
station = Station.objects.get(pk=1)
start_rental(customer, station, current_date)


customer = Customer.objects.get(pk=2)
station = Station.objects.get(pk=1)
start_rental(customer, station, current_date)


# rental = Rental.objects.get(pk=1)
# end_rental(rental,Station.objects.get(pk=5))


for i in range(NUMBER_OF_DAYS):

    # new day, new rentals
    current_date += DATE_ITER
    
    num_of_rental = randint(MIN_RENT_PER_DAY, MAX_RENT_PER_DAY)
    
    active_rentals = Rental.objects.filter(return_date__isnull = True)
    num_act_rental = len(active_rentals)
    

    for i in range (num_of_rental):
        customer = Customer.objects.get(pk=randint(1, NUMBER_OF_CUSTOMER))
        cust_active_rental = customer.customer_rental.filter(return_date__isnull = True)
        if not cust_active_rental:
            try:
                start_rental(customer, Station.objects.get(pk=randint(1,NUMBER_OF_STATION)), current_date)
                #print(f'{customer} rented something')
            except ValueError:
                pass

    rand_rental_nums = sample(range(1,num_act_rental), num_act_rental - randint(1, num_act_rental))

    for j in rand_rental_nums:
        try:
            end_rental(active_rentals[j],Station.objects.get(pk=randint(1, NUMBER_OF_STATION)))
            #print(f'{active_rentals[j]} closed')
        except ValueError:
            pass

    








    
    









