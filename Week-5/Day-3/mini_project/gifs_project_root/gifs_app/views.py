from django.shortcuts import render
from .forms import GifForm
from .models import Gif, Category

def index(request):
    form = GifForm()
    
    
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    
    return render(request,'gifs_app/index.html', context)

# Create your views here.

def all_gifs(request): 

    gifs_list = Gif.objects.all()
    context = {'gifs_list':gifs_list}
    return render(request, 'gifs_app/gifs.html', context)

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





