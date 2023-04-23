from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal,Family

def all_animals(request): 

    animals_list = Animal.objects.all()
    context = {'animals': animals_list}

    return render(request, 'animals.html', context)


def animal (request, id:int):
    animals_list = Animal.objects.get(id=id)
    animal_instance = find_instance(animals_list, id)
    context = {'animal': animal_instance}

    return render(request, 'animal.html', context)