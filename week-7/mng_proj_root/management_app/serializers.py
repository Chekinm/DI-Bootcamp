from .models import Employee, Department, Task, Project
from rest_framework import serializers

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detailed' )
    deparment = serializers.HyperlinkedIdentityField(view_name='department-detailed')
    project = serializers.HyperlinkedIdentityField(view_name='project-detailed',many=True)
    class Meta:
        model = Employee
        fields = '__all__'

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='department-detailed' )
    
    class Meta:
        model = Department
        fields = '__all__'

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detailed' )
    project = serializers.HyperlinkedIdentityField(view_name='project-detailed')
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='project-detailed')
    class Meta:
        model = Project
        fields = '__all__'
