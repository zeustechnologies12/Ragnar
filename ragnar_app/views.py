from rest_framework import viewsets
from .models import *
from .serializers import *

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
