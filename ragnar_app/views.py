from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action in ['signup', 'login']:
            return [] 
        return [IsAuthenticated()]
    @action(detail=False, methods=['post'], url_path='signup', url_name='signup-user')
    def signup(self, request):    
        data = request.data
        if data.get('password'):
            data['password'] = make_password(data.get('password'))
        else:
            return Response({"message":"Password is required"},status=status.HTTP_400_BAD_REQUEST)
        if 'role' not in data:
             return Response({"message":"Role is required"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            role = data.get('role')
            try:
                group = Group.objects.get(name = role)
            
            except:
                return Response({"message": f"Role {role} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            
            user  = serializer.save()
            user.groups.add(group)
            
            return Response({
                "succes":True,
                "data":self.get_serializer(user).data,
                "message":"User Created Successfully",
            },status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login', url_name='login-user')
    def login(self,request):
        data = request.data
        if not data.get('password') :
            return Response({"message":"Password is required"},status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email = data.get('email')) 
        if not user:
            return Response({"message":"User not found"},status=status.HTTP_400_BAD_REQUEST)
        
        password = data.get('password')
        if(check_password( password,user.password)):
            user_groups = {group.id: group.name for group in user.groups.all()}
            user_data = self.get_serializer(user).data
            refresh = RefreshToken.for_user(user) 
            return Response({
            "succes":True,
            "data":user_data,
            "message":"Logged In Successfully",
            "user":user.email,
            "tokens":{
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
            "roles": user_groups, 
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
   
        