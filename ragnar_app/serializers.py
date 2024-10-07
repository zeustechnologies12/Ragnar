from rest_framework import serializers
from .models import *

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name','last_name', 'email','cnic', 'phone_number','password']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True)    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number','password']