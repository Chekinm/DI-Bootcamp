from django.db import models
from django.db.models.signals import post_save


class Address(models.Model):
    """general table, represent all addresses somehow entered into DB"""
    
    house       = models.CharField(max_length=50)
    street      = models.CharField(max_length=250)    
    city        = models.CharField(max_length=150)
    country     = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=50)  

    def __str__(self):
        return f'{self.street}, {self.house}\n{self.postal_code}, {self.country}, {self.city}'  

    
class Customer(models.Model):
    """Table stores customers details"""
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=254)
    number      = models.CharField(max_length=40, unique=True)
    address     = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Station(models.Model):
    """Table stores rental station inforation"""    
    name    = models.CharField(max_length=250)
    number  = models.CharField(max_length=40, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class VehicleType(models.Model):
    """possible type of vehicle (one-to-many relations with vehicle)"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    """possible size of vehicle (one-to-many relations with vehicle)"""
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    """Vehichle table""" 
    class Status(models.IntegerChoices):
        RENTED = 0
        ON_STATION = 1
        NO_WHERE = 2

    vehicle_type    = models.ForeignKey(VehicleType, on_delete=models.CASCADE) 
    size            = models.ForeignKey(VehicleSize, on_delete=models.CASCADE) 
    date_created    = models.DateField(auto_now_add=True)
    real_cost       = models.FloatField()
    status          = models.IntegerField(choices=Status.choices, default=2)   
    
    class Meta:
        ordering = ('vehicle_type','size',)

    def __str__(self):
        return f'{self.size} {self.vehicle_type}'
    
    @property
    def status_string(self):

        rentals = self.vehicles_rentals

        if self.status == 2:  # NO_WHERE
            return f'''Vehicle is is not at the staion yet'''
        
        elif self.status == 0: # RENTED
            last_rental = rentals.order_by('-start_date')[0]
            last_renter = last_rental.customer 
            last_station_record = self.vehicles_station_record.order_by('-arrival_date')[0]
            last_station = last_station_record.station.name
            return f'''Vehicle is currently rented by {last_renter}\n
                It was rented on {last_rental.start_date}, at the {last_station} rental station.'''
        
        else:   # AVIALABLE AT STATION
            last_station_record = self.vehicles_station_record.order_by('-arrival_date')[0]
            last_station = last_station_record.station.name
            return f'''Vehicle is currently availble for rent  at {last_station} rental station.'''


class RentalRate(models.Model):
    """price list"""
    daily_rate      = models.FloatField()
    vehicle_type    = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size    = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_size} {self.vehicle_type} : {self.daily_rate}'
    

class Rental(models.Model):
    """talbe stores rental transaction with. 
        Each rental has a vehicle, customer, and rental_start date.
        rental_end_date can be NULL, which means that rental is currently active 
        """
    start_date   = models.DateField(blank=False)
    return_date  = models.DateField(null=True, blank=True)
    customer     = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_rental')
    vehicle      = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles_rentals')

    def __str__(self):
        if self.return_date == None:
            return f'Start date: {self.start_date}, Not returned yet!'
        return f'Start date: {self.start_date}, end date: {self.return_date}'
    

class VehicleAtStation (models.Model):
    """table stores each transaction, when vehicle is not rented, but on  
        the rental station.
        Each VehiclAtStation event has a vehicle, rentalstations, and arrival_date
        depature_date can be NULL, which means that vehicle is on rental station now"""
    
    arrival_date    = models.DateField(blank=False)
    departure_date  = models.DateField(null=True, blank=True)
    vehicle         = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicles_station_record')
    station         = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='vehicle_at_station')
    
    def __str__(self):
        return f'{self.arrival_date}, {self.departure_date}'
    

# def send_to_station(sender, instance, created, **kwargs):
#     station, current_date = Station.objects.get(id=1), date.today()
#     new_vehicle_at_station = VehicleAtStation(
#             arrival_date    = current_date,
#             # departure_date is empty means vehicl is free to rent
#             vehicle         = instance,
#             station         = station,
#                     )

#     new_vehicle_at_station.save()
#     print(f"VEHICLE {instance} sent to {station}")
#     return new_vehicle_at_station


# post_save.connect(receiver=send_to_station, sender=Vehicle)