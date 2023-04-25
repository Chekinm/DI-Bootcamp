from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    category = models.ManyToManyField('Category',blank=True)

    def __str__ (self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

# Create a Category Model with the following fields :

# name (CharField)
# gifs - (many-to-many field with the Gif Model). A Gif can have many different categories, and a category can be shared among many gifs

# Populate the categories: Add around 10 categories to your database using the django shell or the admin. You can find some ideas of gif categories on the giphy website - categories
