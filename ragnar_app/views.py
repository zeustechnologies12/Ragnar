from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def create(self,request):
        data = request.data
        data['password'] = make_password(data.get('password'))
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            manager = serializer.save()
            return Response({
                "message":"Manager Created Successfully",
                "manager":manager.first_name,
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):    
        data = request.data
        data['password'] = make_password(data.get('password'))
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user  = serializer.save()
            return Response({
                "message":"User Created Successfully",
                "User":user.first_name,
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        