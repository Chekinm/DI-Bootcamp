from django.urls import path
from .views import *

urlpatterns = [
    path('employees', EmployeesViewSet.as_view({'get':'list', 'post':'create'}), name='employees'), 
    path('employees/<int:pk>', EmployeeDetailedViewSet.as_view({'get':'retrieve', 'put':'update'}), name='employee-detailed'), 

    path('departments', DepartmentsViewSet.as_view({'get':'list', 'post':'create'}), name='departments'), 
    path('departments/<int:pk>', DepartmentDetailedViewSet.as_view({'get':'retrieve', 'put':'update'}), name='department-detailed'), 
    
    path('tasks', TasksViewSet.as_view({'get':'list', 'post':'create'}), name='tasks'), 
    path('tasks/<int:pk>', TaskDetailedViewSet.as_view({'get':'retrieve', 'delete':'destroy','put':'update'}), name='task-detailed'), 
    
    path('projects', ProjectsViewSet.as_view({'get':'list', 'post':'create'}), name='projects'),
    path('projects/<int:pk>', ProjectDetailedViewSet.as_view({'get':'retrieve', 'delete':'destroy','put':'update'}), name='project-detailed'),
]

