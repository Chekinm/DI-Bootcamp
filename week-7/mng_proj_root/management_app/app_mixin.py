from rest_framework import mixins
from .models import Department, Employee, Task, Project
from .serializers import EmployeeSerializer, DepartmentSerializer
from .serializers import TaskSerializer, ProjectSerializer
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

class DepartmentOperationsMixin (ListModelMixin, CreateModelMixin):
    queryset =  Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeOperationsMixin (ListModelMixin, CreateModelMixin):
    queryset =  Employee.objects.all()
    serializer_class = EmployeeSerializer


class TaskOperationsMixin (ListModelMixin, CreateModelMixin, 
                           UpdateModelMixin, DestroyModelMixin):
                                
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer


class ProjectOperationsMixin (ListModelMixin, CreateModelMixin, 
                            UpdateModelMixin, DestroyModelMixin):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer


