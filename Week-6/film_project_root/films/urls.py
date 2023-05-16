from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('add_film/', views.AddFilm.as_view(), name='add_film'),
    path('add_director/', views.AddDirector.as_view(), name='add_director'),
    path('update_film/<int:pk>/', views.UpdateFilm.as_view(), name='update_film'),
    path('update_director/<int:pk>/', views.UpdateDirector.as_view(), name='update_director'),

]

