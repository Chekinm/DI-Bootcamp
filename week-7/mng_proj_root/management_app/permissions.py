from .models import Employee, Department, Task, Project
from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
   
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.db_user.role == 'dep_adm':
            return True
        return False
   
