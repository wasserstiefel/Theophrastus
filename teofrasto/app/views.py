from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Architect, Firm, Project, Client
from .serializers import ArchitectSerializer, FirmSerializer, ProjectSerializer, ClientSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'PUT','DELETE'])
def Architects(request, id):
    architect = get_object_or_404(Architect, pk=id)
    if request.method == 'GET':
        serializer =  ArchitectSerializer(architect)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArchitectSerializer(architect, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        architect.delete()
        id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT','DELETE'])
def Firms(request, id):
    firm  = get_object_or_404(Firm, pk=id)
    if request.method == 'GET':
        serializer = FirmSerializer(firm)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FirmSerializer(firm, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT','DELETE'])
def Projects(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT','DELETE'])
def Clients(request, id):
    client =  get_object_or_404(Client, pk=id)
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Firm_List(request):
    if request.method == 'GET':
        queryset = Firm.objects.all()
        seralizer = FirmSerializer(queryset, many=True)
        return Response(seralizer.data)
    elif request.method == 'POST':
        serializer = FirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def Architect_List(request):
    if request.method == 'GET':
        queryset = Architect.objects.select_related('firm').prefetch_related('project').all()
        serializer = ArchitectSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArchitectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def Project_List(request):
    if request.method == 'GET':
        queryset = Project.objects.all()
        serializer  = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =  ProjectSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])    
def Client_List(request):
    if request.method == 'GET':
        queryset = Client.objects.all()
        serializer  = ClientSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =  ClientSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data, status=status.HTTP_201_CREATED)