from django.shortcuts import render
from django.http import HttpResponse
from . import utils


def index (request):
    
    return render (request, 'index.html')


def all_animals (request):
    animals_list = utils.read_data('data.json','animals')
    context = {'animals_list':animals_list}
    return render (request, 'animals.html', context)

def one_animal (request, id:int):
    animals_list = utils.read_data('data.json','animals')
    animal = utils.read_instance(animals_list, id)
    context = {'animal':animal}
    return render (request, 'one_animal.html', context)

def all_families (request):
    families_list = utils.read_data('data.json','families')
    context = {'families_list':families_list}
    return render (request, 'families.html', context)
                                
def one_family (request, id:int):
    families_list = utils.read_data('data.json','families')
    animals_list = utils.read_data('data.json','animals')
    family = utils.read_instance(families_list, id)
    families_animals_list = utils.read_animal_by_family(animals_list, id)
    context = {'family':family,
               'families_animals_list':families_animals_list}
    return render (request, 'one_family.html', context)

