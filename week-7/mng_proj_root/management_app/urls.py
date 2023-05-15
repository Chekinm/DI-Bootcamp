from django.urls import path
from .views import *

urlpatterns = [
    path('employees', EmployeesView.as_view(), name='employees'), 
    path('departments', DepartmentsView.as_view(), name='departments'), 
    path('tasks', TasksView.as_view(), name='tasks'), 
    path('tasks/<int:pk>', TaskView.as_view(), name='task'), 
    path('projects', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectView.as_view(), name='project'),
]

