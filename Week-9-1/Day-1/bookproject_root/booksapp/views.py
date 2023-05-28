from django.shortcuts import render, redirect
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from django.urls import reverse, reverse_lazy

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def book_create(request):
    print(request.POST)
    if request.method == 'POST':
        
        serializer = BookSerializer(data=request.POST)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse_lazy('book-list'))
        else:
            print(serializer.errors)
            
        
    else:
        serializer = BookSerializer()
    return render(request, 'book.html', {'serializer': serializer})