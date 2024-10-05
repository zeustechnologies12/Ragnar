from django.db import models
from django_softdelete.models import SoftDeleteModel

class Manager(SoftDeleteModel,models.Model):
    first_name  = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15,unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'managers'
    
class User(SoftDeleteModel,models.Model):
    first_name  = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
    
   
   


