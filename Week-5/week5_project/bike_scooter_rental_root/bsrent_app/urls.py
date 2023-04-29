from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('add_user/', views.add_user, name='add_user'),


    path('rent/', views.rent, name='rent'), #main page 


    path('all_customers/', views.all_customers, name='all_customers'),
    path("all_customers/<int:id>/", views.one_customer, name="one_customer"),



    # path('stations', views.all_stations, name='all_stations'),  
    # path('vehicles', views.all_vehicles, name='all_vehicles'),  
    # path('retnals', views.all_rentals, name='all_customers'),   







]

