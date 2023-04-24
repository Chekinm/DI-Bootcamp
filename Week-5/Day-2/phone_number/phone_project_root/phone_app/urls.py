from django.urls import path

from . import views

urlpatterns = [
    path("persons/", views.all_persons, name="all_persons"),
    path("persons/<str:search_value>", views.person_details, name="persons_details"),
    
    # path("animals/<int:id>/", views.one_animal, name="one_animal"),
    # path("families/", views.all_families, name="all_families"),
    # path("families/<int:id>/", views.one_family, name="one_family"),
]