from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    context = 'Test Page'
    return render(request, 'test_app/index.html', context)