from django.urls import path
from . import views

urlpatterns = [
    path('todo_view', views.todo_view, name='todo_view'),
    path('add_todo', views.add_todo, name='add_todo'),
]

