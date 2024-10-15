from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def create(self,request):
        data = request.data
        if data.get('password'):
            data['password'] = make_password(data.get('password'))
        else:
            return Response({"message":"Password is required"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            manager = serializer.save()
            return Response({
                "message":"Manager Created Successfully",
                "manager":manager.first_name,
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    @action(detail=False, methods=['post'], url_path='login', url_name='login-user')
    def login(self,request):
        data = request.data
        manager = Manager.objects.get(email = data.get('email'))
        password = data.get('password')
        if(check_password( password,manager.password)):
            return Response({
            "message":"Manager Logged In Successfully",
            "user":manager.email
            },status=status.HTTP_200_OK)
        else:
            return Response({
            "message":"Could not authenticate Manager"
            },status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):    
        data = request.data
        if data.get('password'):
            data['password'] = make_password(data.get('password'))
        else:
            return Response({"message":"Password is required"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user  = serializer.save()
            return Response({
                "message":"User Created Successfully",
                "User":user.first_name,
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login', url_name='login-user')
    def login(self,request):
        data = request.data
        user = User.objects.get(email = data.get('email'))
        password = data.get('password')
        if(check_password( password,user.password)):
            return Response({
            "message":"Logged In Successfully",
            "user":user.email
            },status=status.HTTP_200_OK)
        else:
            return Response({
            "message":"Could not authenticate user"
            },status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='restore', url_name='restore')
    def restore(self,request,pk):
       try:
           user = User.deleted_objects.get(pk=pk)
           user.restore()
           return Response({
               "message":"User restored successfully",
               "user":user.first_name
           },status=status.HTTP_200_OK)
       except User.DoesNotExist:
           return Response({
                "error": "Not found"
            }, status=status.HTTP_404_NOT_FOUND)    
   
        