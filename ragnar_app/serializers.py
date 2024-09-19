from rest_framework import serializers
from .models import *

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name','last_name', 'email', 'password', 'cnic', 'phone_number']
