from django.contrib import admin
from .models import Customer, Vehicle, VehicleSize, VehicleType, Rental, RentalRate, VehicleAtStation, Station
# Register your models here.
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleSize)
admin.site.register(VehicleType)
admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(VehicleAtStation)
admin.site.register(Station)

