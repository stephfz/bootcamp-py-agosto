from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=45, blank=False, null =False)
    lastname =models.CharField(max_length=45, blank=False, null =False)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
