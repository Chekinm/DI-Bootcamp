from django.db import models

# Create your models here.

class  Category (models.Model):
    """catorgiry tabel to catogorise our todolist
        like work home etc"""
    name = models.CharField(max_length=50)
    image = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name


class ToDoTask (models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=300)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(blank=True, null=True)
    deadline_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Task - {self.title}, created on {self.date_creation}, category - {self.category}, Dealine - {self.deadline_date}, completed - {self.has_been_done}' 
    
    