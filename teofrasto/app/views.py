from itertools import product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Architect, Firm, Project, Client
from .serializers import ArchitectSerializer, FirmSerializer, ProjectSerializer, ClientSerializer
from rest_framework import status

# Create your views here.
class Architects(RetrieveUpdateDestroyAPIView):
    queryset = Architect.objects.all()
    serializer_class = ArchitectSerializer


class Firms(RetrieveUpdateDestroyAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    
    def delete(self, request, pk):
        firm  = get_object_or_404(Firm, pk=pk)
        if firm.client_set.count() > 0 or firm.architect_set.count() > 0:
            return Response({'error': 'firm cannot be eliminated because it is associated with another model'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Projects(RetrieveUpdateDestroyAPIView):
   queryset = Project.objects.all()
   serializer_class = ProjectSerializer



class Clients(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
  

class FirmList(ListCreateAPIView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
   
class ArchitectList(ListCreateAPIView):
    queryset = Architect.objects.select_related('firm').prefetch_related('project').all()
    serializer_class = ArchitectSerializer

class ProjectList(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class  = ProjectSerializer
        
class ClientList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class  = ClientSerializer
        