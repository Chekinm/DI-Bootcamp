from django.urls import path
from . import views

urlpatterns = [
    path('', views.rent, name='rent'), 
    path('rent/', views.rent, name='rent'), #main page 
    path('manage_database/', views.manage_database, name='manage_database'), #if you like to add stuff  

    path("add_address/", views.AddAddress.as_view(), name="add_address"),

    path('all_customers/', views.AllCustomer.as_view(), name='all_customers'),
    path("all_customers/<int:pk>/", views.OneCustomer.as_view(), name="one_customer"),
    path('add_customer/', views.AddCustomer.as_view(), name='add_customer'),



    path('rentals/', views.rentals, name='rentals'),
    path('rentals/open_rentals/', views.OpenRentals.as_view(), name='open_rentals'),
    path('rentals/closed_rentals/', views.ClosedRentals.as_view(), name='closed_rentals'),
    path('rentals/<int:pk>/', views.OneRental.as_view(), name="one_rental"),
    #path('rent_vehicle/<int:id>/', views.rent_vehicle, name="rent_vehicle"),
   
    path('all_stations/', views.AllStations.as_view(), name='all_stations'),
    path("all_stations/<int:pk>/", views.OneStation.as_view(), name="one_station"),
    path("add_station/", views.AddStation.as_view(), name="add_station"),



    path('all_vehicles/', views.AllVehicles.as_view(), name='all_vehicles'),
    path("all_vehicles/<int:pk>/", views.OneVehicle.as_view(), name="one_vehicle"),
    path("add_vehicle/", views.AddVehicle.as_view(), name="add_vehicle"),

    path('test/', views.test)
   

]

