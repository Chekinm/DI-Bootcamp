import os
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_scooter_rental.settings')
django.setup()
from bsrent_app.models import  Address, Customer, Station, RentalRate, Rental, VehicleAtStation, VehicleType, VehicleSize, Vehicle
import datetime
from random import sample, randint, choice





# import os
# from faker import Faker
# from bsrent_app.models import  Address, Customer, Station, RentalRate, Rental, VehicleAtStation, VehicleType, VehicleSize, Vehicle
# import datetime
# from faker import Faker
# from random import sample, randint, choice






def start_rental(vehicle, customer, station, current_date):
    
    # if  vehicle.vehicles_station_record.order_by('-arrival_date')[0].departure_date != None:
    #     raise ValueError('Vehicel is not free at the time')
    # if len(customer.customer_rental.filter(return_date__isnull=True)) > 0:
    #     raise ValueError('Customer cannot rent more thatn one vehicle')
    # if station.vehicle_at_station.filter(departure_date__isnull=True) == 0:
    #     raise ValueError('There is no car at station')
    
    rental = Rental( 
                start_date   = current_date,
                # return_date  empry, means vehicl is on ride now
                customer     = customer,
                vehicle      = vehicle,
                )
    a = vehicle.vehicles_station_record.order_by('-arrival_date')[0]
    a.departure_date  = current_date
    print(a, a.id)
    a.save()  
    print(a, a.id)  
    rental.save()
    return rental

station = Station.objects.get(id=5)
print(station)
customer = Customer.objects.get(id=179)
print(customer)
current_date = datetime.date(2020,1,1)
vehicle = Vehicle.objects.get(id = 7 )

print(start_rental(vehicle, customer, station, current_date))

