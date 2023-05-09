from django.shortcuts import render, redirect
from .models import Employee, Department, Task, Project
from .serializers import EmployeeSerializer, DepartmentSerializer
from .serializers import TaskSerializer, ProjectSerializer

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView 
from rest_framework.generics import CreateAPIView, DestroyAPIView

from .app_mixin import EmployeeOperationsMixin, DepartmentOperationsMixin
from .app_mixin import ProjectOperationsMixin, TaskOperationsMixin
from rest_framework.permissions import AllowAny, IsAdminUser
from .permissions import IsDepartmentAdmin

class EmployeesView (EmployeeOperationsMixin, GenericAPIView):

    permission_classes = [IsDepartmentAdmin,]
  
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DepartmentsView (DepartmentOperationsMixin, GenericAPIView):

    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   

class TasksView (TaskOperationsMixin, GenericAPIView):

    permission_classes = (IsDepartmentAdmin,)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
         
    def put(self, request, *args, **kwargs):      
        return self.update(request, *args, **kwargs)


class ProjectsView (ProjectOperationsMixin, GenericAPIView):

    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
         
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
   