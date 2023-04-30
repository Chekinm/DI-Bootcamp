from django.urls import path
from . import views

urlpatterns = [
    path('', views.rent, name='rent'), 
    path('rent/', views.rent, name='rent'), #main page 
    path('manage_database/', views.manage_database, name='manage_database'), #if you like to add stuff  

    path("add_address/", views.AddAddress.as_view(), name="add_address"),

    path('all_customers/', views.all_customers, name='all_customers'),
    path("all_customers/<int:id>/", views.one_customer, name="one_customer"),
    path('add_customer/', views.AddCustomer.as_view(), name='add_customer'),



    path('rentals/', views.rentals, name='rentals'),
    path('rentals/open_rentals/', views.open_rentals, name='open_rentals'),
    path('rentals/closed_rentals/', views.closed_rentals, name='closed_rentals'),
    path('rentals/<int:id>/', views.one_rental, name="one_rental"),
    #path('rent_vehicle/<int:id>/', views.rent_vehicle, name="rent_vehicle"),
   
    path('all_stations/', views.all_stations, name='all_stations'),
    path("all_stations/<int:id>/", views.one_station, name="one_station"),
    path("add_station/", views.AddStation.as_view(), name="add_station"),



    path('all_vehicles/', views.all_vehicles, name='all_vehicles'),
    path("all_vehicles/<int:id>/", views.one_vehicle, name="one_vehicle"),
    path("add_vehicle/", views.AddVehicle.as_view(), name="add_vehicle"),

    path('test/', views.test)
   

]

