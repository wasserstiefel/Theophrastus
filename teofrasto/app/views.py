from distutils import errors
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Architect
from .serializers import ArchitectSerializer
from rest_framework import status

# Create your views here.
@api_view()
def Architects(request, id):
    
        architect = get_object_or_404(Architect, pk=id)
        serializer =  ArchitectSerializer(architect)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def Architect_List(request):
    if request.method == 'GET':
        queryset = Architect.objects.select_related('firm').all()
        seralizer = ArchitectSerializer(queryset, many=True)
        return Response(seralizer.data)
    elif request.method == 'POST':
        seralizer = ArchitectSerializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        seralizer.validated_data
        return Response('ok')
    