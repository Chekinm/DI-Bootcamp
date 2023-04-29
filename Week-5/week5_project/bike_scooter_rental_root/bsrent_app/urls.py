from django.urls import path
from . import views

urlpatterns = [
    path('', views.rent, name='rent'), 
    path('rent/', views.rent, name='rent'), #main page 


    path('all_customers/', views.all_customers, name='all_customers'),
    path("all_customers/<int:id>/", views.one_customer, name="one_customer"),
    #path('add_all_customers/', views.add_user, name='add_user'),



    path('rentals/', views.rentals, name='rentals'),
    path('rentals/open_rentals/', views.open_rentals, name='open_rentals'),
    path('rentals/closed_rentals/', views.closed_rentals, name='closed_rentals'),
    path('rentals/<int:id>/', views.one_rental, name="one_rental"),
    #path('rent_vehicle/<int:id>/', views.rent_vehicle, name="rent_vehicle"),
   
    path('all_stations/', views.all_stations, name='all_stations'),
    path("all_stations/<int:id>/", views.one_station, name="one_station"),
    #path("add_stations/<int:id>/", views.add_station, name="add_station"),



    path('all_vehicles/', views.all_vehicles, name='all_vehicles'),
    path("all_vehicles/<int:id>/", views.one_vehicle, name="one_vehicle"),



    # path('stations', views.all_stations, name='all_stations'),  
    # path('vehicles', views.all_vehicles, name='all_vehicles'),  
    # path('retnals', views.all_rentals, name='all_customers'),   







]

