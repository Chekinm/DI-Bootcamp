import os
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_scooter_rental.settings')
django.setup()
from bsrent_app.models import  Address, Customer, Station, RentalRate, Rental, VehicleAtStation, VehicleType, VehicleSize, Vehicle
import datetime
from random import sample, randint, choice

fake = Faker()

START_DATE = datetime.date(2018, 1, 1)
DATE_ITER = datetime.timedelta(2)
current_date = datetime.date(2018, 1, 1)
NUMBER_OF_CUSTOMER = 1000
NUMBER_OF_STATION = 10
NUMBER_OF_VEHICLE = 300

# create 5000 addresses and customers

for i in range(NUMBER_OF_CUSTOMER):

    house       = fake.building_number()
    street      = fake.street_name() 
    city        = fake.city()
    country     = fake.country()
    postal_code = fake.postcode()
    

    new_address = Address(
                        house       = house,
                        street      = street, 
                        city        = city,
                        country     = country,
                        postal_code = postal_code,
                        )

    first_name  = fake.first_name(), 
    last_name   = fake.last_name(),
    email       = fake.email()
    number      = fake.phone_number()
    address     = new_address
    
    new_customer = Customer(
                        first_name = first_name[0],  
                        last_name = last_name[0],
                        email = email,  
                        number = number, 
                        address = address,
                         )
    
    new_address.save()
    new_customer.save()

# create 10 rental station

for i in range(NUMBER_OF_STATION):

    house       = fake.building_number()
    street      = fake.street_name() 
    city        = fake.city()
    country     = fake.country()
    postal_code = fake.postcode()
    
    new_address = Address(
                    house       = house,
                    street      = street, 
                    city        = city,
                    country     = country,
                    postal_code = postal_code,
                    )

    number      = fake.phone_number()
    address     = new_address
    capacity    = 1000
    new_rental_station = Station(
                        name = street,  
                        number = number, 
                        address = address,
                        capacity = capacity,
                        )
    
    new_address.save()
    new_rental_station.save()


# create 3 sizes and types of vehicle
type_list = [0 for i in range(3)]
size_list = [0 for i in range(3)]


size_list[0] = VehicleSize(name = 'small')
size_list[1] = VehicleSize(name = 'medium')
size_list[2] = VehicleSize(name = 'big')

type_list[0] = VehicleType(name = 'scooter')
type_list[1] = VehicleType(name = 'bike')
type_list[2] = VehicleType(name = 'electro bike')

base_rate = 5.0

index = 0
coef = 2
for tp in type_list:
    tp.save()
    index = 2.1
    for sz in size_list:
        sz.save()
        rate = base_rate * coef + index 
        daily_rate_list = RentalRate(
            daily_rate      = rate,
            vehicle_type    = tp,
            vehicle_size    = sz,
        )
        daily_rate_list.save()
        index += 4.7
    coef += 2

#create 1000 random Vehicle

for i in range(NUMBER_OF_VEHICLE):

    rnd1 = randint(0,2)
    rnd2 = randint(0,2)

    vt = type_list[rnd1]
    sz = size_list[rnd2]

    date_created = START_DATE

    real_cost = (randint(100, 120)*(rnd1 + 1) + randint(25, 50)*(rnd2 + 1)) 
    new_vehicle = Vehicle(
                    vehicle_type   = vt,
                    size           = sz,
                    real_cost      = real_cost,
                    date_created = START_DATE,
                    status          = 2
                    ) 

    new_vehicle.save()


# let's take all vehicle and randomly seed it to rental stations

all_vehicle = Vehicle.objects.all() # list of vehicle objects
all_rental_station = Station.objects.all() #list of station objects



for vehicle in all_vehicle:
# take each vehicle and put it into one of the station
    arrival_date    = current_date
    station         = choice(all_rental_station)
    new_vehicle_at_station = VehicleAtStation(
                        arrival_date    = arrival_date,
                        # depature_date is empty -> NULL, means vehicl is on station now
                        vehicle         = vehicle,
                        station         = station,
                        )
    vehicle.status = 1
    vehicle.save()
    new_vehicle_at_station.save()





