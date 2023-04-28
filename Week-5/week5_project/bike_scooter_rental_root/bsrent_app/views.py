from django.shortcuts import render
from .models import TestModel, Customer
from .forms import TestForm, CustomerForm

def index (request):
    test = Customer.objects.all()
    print(test[0])
    context = {'content':test[0],
               'greeting':'Hello'}
    
    return render(request, 'bsrent_app/index.html', context)

def add_user (request):
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form_content':form}

    if request.method == 'GET':
       
        form = CustomerForm()
        print(form)
        context = {'form_content':form}

    
    return render(request, 'bsrent_app/add_user.html', context)

