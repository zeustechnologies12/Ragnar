from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True)    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_number','password','role']