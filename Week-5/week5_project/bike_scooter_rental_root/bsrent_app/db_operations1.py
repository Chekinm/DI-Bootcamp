import os
from faker import Faker
from .models import  Address, Customer, Station, RentalRate, Rental, VehicleAtStation, VehicleType, VehicleSize, Vehicle
import datetime
from faker import Faker
from random import sample, randint, choice


def start_rental(vehicle, customer, station, current_date):
    
    if  vehicle.vehicles_station_record.order_by('-arrival_date')[0].depature_Date != None:
        raise ValueError('Vehicel is not free at the time')
    if len(customer.customer_rental.filter(return_date__isnull=True)) > 0:
        raise ValueError('Customer cannot rent more thatn one vehicle')
    if station.vehicle_at_station.filter(departure_date__isnull=True) == 0:
        raise ValueError('There is no car at station')
    
    rental = Rental( 
                start_date   = current_date,
                # return_date  empry, means vehicl is on ride now
                customer     = customer,
                vehicle      = vehicle,
                )
    at_station_record = vehicle.vehicles_station_record.order_by('-arrival_date')[0]
    at_station_record.departure_date  = current_date
    at_station_record.save()
    rental.save()
    return rental



def send_to_station(vehicle, station, date):
    
    new_vehicle_at_station = VehicleAtStation(
            arrival_date    = current_date,
            # departure_date is empty means vehicl is free to rent
            vehicle         = vehicle,
            station         = station,
                    )
    vehicle.status = ON_STATION
    vehicle.save()
    new_vehicle_at_station.save()
    return new_vehicle_at_station

# station = Station.objects.get(id=5)
# print(station)
# customer = Customer.objects.get(id=179)
# print(customer)
# current_date = datetime.date(2020-1-1)
# vehicel = Vehicle.objects.get(id = 7 )

# print(start_rental(vehicle, customer, station, current_date))

