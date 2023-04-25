from django.shortcuts import render
from .data_classes import Animal, Animals, Families, Family

def index (request):
    
    return render (request, 'animal_app/index.html')


def all_animals (request):

    animals = Animals('data.json')
    context = {'animals_list':animals.list}

    return render (request, 'animal_app/animals.html', context)

def one_animal (request, id:int):

    animals = Animals('data.json')
    animal = Animal(animals, id)
    context = {'animal':animal.data}
    return render (request, 'animal_app/one_animal.html', context)

def all_families (request):
    families = Families('data.json')
    context = {'families_list':families.list}
    return render (request, 'animal_app/families.html', context)
                                
def one_family (request, id:int):
    families = Families('data.json')
    animals = Animals('data.json')
    family = Family(families, id)
    
    family.get_family_memebers(animals)

    context = {'family':family.data,
               'families_animals_list':family.animals_list}
    
    return render (request, 'animal_app/one_family.html', context)

