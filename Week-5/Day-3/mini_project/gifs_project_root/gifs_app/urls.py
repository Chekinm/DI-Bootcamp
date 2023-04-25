from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='something'),
    path('gifs/', views.all_gifs, name='all_gifs'),
    


]
