from django.urls import path

from . import views

urlpatterns = [
    path("animals/", views.all_animals, name="all_animals"),
    path("animals/<int:id>/", views.one_animal, name="one_animal"),
    path("families/", views.all_families, name="all_families"),
    path("families/<int:id>/", views.one_family, name="one_family"),
]  