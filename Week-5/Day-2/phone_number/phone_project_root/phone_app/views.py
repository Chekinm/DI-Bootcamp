from django.shortcuts import render
from django.http import HttpResponse
from phone_app.models import Person
# Create your views here.




def all_persons(request): 

    persons_list = Person.objects.all()
    
    context = {'persons_list':persons_list}
    return render(request, 'persons.html', context)



def search(model, value):

    result = None
    try:
        model_instance = model.objects.get(name = value)
        result = model_instance
    except model.DoesNotExist:
        pass
    try:
        model_instance = model.objects.get(phone = value)
        result = model_instance
    except model.DoesNotExist:
        pass

    return result


def person_details(request, search_value:str):

    context = {}

    person = search(Person, search_value)

    if person is not None:
        context = {'person': person}

    return render(request, 'person_datails.html', context)

