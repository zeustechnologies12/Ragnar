from django.db import models
from django_softdelete.models import SoftDeleteModel
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin    
from .enums import *
class User(SoftDeleteModel,AbstractBaseUser,PermissionsMixin):
    first_name  = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,unique=True)
    ROLE_CHOICES = [(role.value, role.name) for role in Role]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    

    class Meta:
        db_table = 'users'
    
   
   


