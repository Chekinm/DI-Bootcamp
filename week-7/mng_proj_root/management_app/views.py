from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from .app_mixin import EmployeeOperationsMixin, DepartmentOperationsMixin
from .app_mixin import ProjectOperationsMixin, TaskOperationsMixin
from rest_framework.permissions import AllowAny, IsAdminUser
from .permissions import IsDepartmentAdmin


class EmployeesViewSet (EmployeeOperationsMixin, GenericViewSet):

    permission_classes = [IsDepartmentAdmin,]

class EmployeeDetailedViewSet (EmployeeOperationsMixin, GenericViewSet):

    permission_classes = [IsDepartmentAdmin,]
      

class DepartmentsViewSet (DepartmentOperationsMixin, GenericViewSet):

    permission_classes = (IsDepartmentAdmin,)
    
    
class DepartmentDetailedViewSet (DepartmentOperationsMixin, GenericViewSet):

    permission_classes = (IsDepartmentAdmin,)
    

class TasksViewSet (TaskOperationsMixin, GenericViewSet):

    permission_classes = (AllowAny,)
        

class TaskDetailedViewSet (TaskOperationsMixin, GenericViewSet):

    permission_classes = (AllowAny,)
    
class ProjectsViewSet (ProjectOperationsMixin, GenericViewSet):

    permission_classes = (AllowAny,)
    
    
class ProjectDetailedViewSet (ProjectOperationsMixin, GenericViewSet):

    permission_classes = (AllowAny,)

    # don't need is with viewset    
    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
         
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
   