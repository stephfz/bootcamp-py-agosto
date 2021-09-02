from django.db import models

import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = 'El nombre debe tener mas de 2 caracteres'
        if len(postData['lastname']) < 2:
            errors['lastname'] = 'El Apellido debe tener mas de 2 caracteres'
        if len(postData['email']) < 2:
            errors['email'] = 'El Correo Electronico debe tener mas de 2 caracteres'
        if len(postData['email']) > 0:
            errors['email'] = self.checkEmail(postData['email'])
        return errors 
    
    def checkEmail(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data):
            errors['email'] = "Correo Invalido"    
        return errors                


class User(models.Model):
    name = models.CharField(max_length=45, blank=False, null =False)
    lastname =models.CharField(max_length=45, blank=False, null =False)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Director(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nationality = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Actor(models.Model):
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
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
    #manytomany
    actors = models.ManyToManyField(Actor)   


  


