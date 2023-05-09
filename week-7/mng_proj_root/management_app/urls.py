from django.urls import path
from .views import *

urlpatterns = [
    path('employees', EmployeesView.as_view(), name='employees'), 
    path('departments', DepartmentsView.as_view(), name='departments'), 
    path('tasks', TasksView.as_view(), name='tasks'), 
    path('projects', ProjectsView.as_view(), name='projects'),
]

