from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True,write_only = True)    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number','password']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number']