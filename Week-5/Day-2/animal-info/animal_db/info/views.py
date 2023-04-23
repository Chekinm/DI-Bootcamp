from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal,Family

def all_animals(request): 

    animals_list = Animal.objects.all()
    context = {'animals_list':animals_list}
    return render(request, 'animals.html', context)

def one_animal (request, id:int):
    animal = Animal.objects.get(id=id)
    #animal = utils.read_instance(animals_list, id)
    context = {'animal':animal}
    return render (request, 'one_animal.html', context)

def all_families (request):
    families_list = Family.objects.all()
    context = {'families_list':families_list}
    return render (request, 'families.html', context)
                                
def one_family (request, id:int):
    family = Family.objects.get(id=id)
    families_animals_list = Animal.objects.filter(family__id=id)
    
    

    context = {'family':family,
               'families_animals_list':families_animals_list}
    return render (request, 'one_family.html', context)

