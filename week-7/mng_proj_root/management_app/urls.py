from django.urls import path
from .views import *

urlpatterns = [
    path('employees', EmployeesView.as_view(), name='employees'), 
    path('employees/<int:pk>', EmployeeDetailedView.as_view(), name='employee-detailed'), 
    path('employees/<int:pk>', EmployeeDetailedView.as_view(), name='user-detail'), 
    path('departments', DepartmentsView.as_view(), name='departments'), 
    path('departments/<int:pk>', DepartmentDetailedView.as_view(), name='department-detailed'), 
    path('tasks', TasksView.as_view(), name='tasks'), 
    path('tasks/<int:pk>', TaskDetailedView.as_view(), name='task-detailed'), 
    path('projects', ProjectsView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetailedView.as_view(), name='project-detailed'),
]

