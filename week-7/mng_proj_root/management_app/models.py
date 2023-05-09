from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
 
    def __str__(self):
        return self.name

ROLE_CHOICES = (
   ('dep_adm', 'Department Admin'), # should be manage departmens and adding user there
   ('hr', 'Human Resource'), # should create users
   ('proj_admin','Project admin') # should manage task and projects
)
    
    



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,related_name='db_user')
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    phone_number  = models.CharField(max_length=15, blank=True)
    deparment = models.ForeignKey('Department', on_delete=models.SET_NULL, related_name='employees', null=True)
    project = models.ManyToManyField('Project', related_name='projects',null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Task(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=False, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
ROLE_CHOICES = (
   ('dep_adm', 'Department Admin'), # should be manage departmens and adding user there
   ('hr', 'Human Resource'), # should create users
   ('proj_admin','Project admin') # should manage task and projects
)
    
    
