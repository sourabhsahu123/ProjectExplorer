from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.FilePathField(path="img")
class Category(models.Model):
    name = models.CharField(max_length=20)
class Post(models.Model):
    title = models.CharField(max_length=255) 
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="img/",default='img/Lion_waiting_in_Nambia.jpg') #default lion 
    categories = models.ManyToManyField('Category',related_name='posts') #one project can have multiple post. General category.
    #post is for the reference.
    projects = models.ManyToManyField('Project',related_name='project')

 # when you do make migrations it creates a file from models.