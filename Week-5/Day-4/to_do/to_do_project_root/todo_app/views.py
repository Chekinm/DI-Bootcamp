from django.shortcuts import render
from .models import Category, ToDoTask
from .forms import ToDoForm


def todo_view(request):
    todo_list = ToDoTask.objects.all()
    
    context = {'todo_list': todo_list} 
    return render(request, 'todo_app/todo_view.html', context)

def add_todo(request):

    form = ToDoForm(wedgets)

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid(): 
            form.save()

    context = {'form': form} 
    return render(request, 'todo_app/add_todo.html', context)

# Create your views here.
