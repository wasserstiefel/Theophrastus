from itertools import product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Architect, Firm, Project, Client
from .serializers import ArchitectSerializer, FirmSerializer, ProjectSerializer, ClientSerializer
from rest_framework import status

# Create your views here.
class Architects(APIView):
    def get(self, request, id):
        architect = get_object_or_404(Architect, pk=id)
        serializer =  ArchitectSerializer(architect)
        return Response(serializer.data)

    def put(self, request, id):
        architect = get_object_or_404(Architect, pk=id)
        serializer = ArchitectSerializer(architect, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        architect = get_object_or_404(Architect, pk=id)
        architect.delete()
        id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Firms(APIView):
    def get(self, request, id):
        firm  = get_object_or_404(Firm, pk=id)    
        serializer = FirmSerializer(firm)
        return Response(serializer.data)

    def put(self, request, id):
        firm  = get_object_or_404(Firm, pk=id)    
        serializer = FirmSerializer(firm, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        firm  = get_object_or_404(Firm, pk=id)
        if firm.client_set.count() > 0 or firm.architect_set.count() > 0:
            return Response({'error': 'firm cannot be eliminated because it is associated with another model'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Projects(APIView):
    def get(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, id):
        project = get_object_or_404(Project, pk=id)
        serializer = ProjectSerializer(project, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request,id):
        project = get_object_or_404(Project, pk=id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Clients(APIView):
    def get(self, request, id):
        client =  get_object_or_404(Client, pk=id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, id):
        client =  get_object_or_404(Client, pk=id)
        serializer = ClientSerializer(client, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        client =  get_object_or_404(Client, pk=id)     
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FirmList(APIView):
    def get(self, request):
        queryset = Firm.objects.all()
        seralizer = FirmSerializer(queryset, many=True)
        return Response(seralizer.data)

    def post(self, request):
        serializer = FirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArchitectList(APIView):
    def get(self, request):
        queryset = Architect.objects.select_related('firm').prefetch_related('project').all()
        serializer = ArchitectSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArchitectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectList(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        serializer  = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =  ProjectSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClientList(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer  = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer =  ClientSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)