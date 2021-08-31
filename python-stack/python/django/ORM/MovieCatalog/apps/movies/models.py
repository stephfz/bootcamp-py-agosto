from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=45, blank=False, null =False)
    lastname =models.CharField(max_length=45, blank=False, null =False)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

class Director(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nationality = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, related_name='movies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)    


  


