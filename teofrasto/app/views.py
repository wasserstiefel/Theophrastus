from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Architect, Firm, Project, Client
from .serializers import ArchitectSerializer, FirmSerializer, ProjectSerializer, ClientSerializer

# Create your views here.

class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends =  [SearchFilter]
    search_fields = ['firm_name','country', 'address']

    def destroy(self, request, *args, **kwargs):
        if Client.objects.filter(firm_id=kwargs['pk']).count() > 0 or Architect.objects.filter(firm_id=kwargs['pk']).count() > 0:
            return Response({'error': 'firm cannot be eliminated because it is associated with another model'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    


class ProjectViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectSerializer
   filter_backends =  [SearchFilter, OrderingFilter]
   search_fields = ['contract_number', 'building_material', 'country_abr', 'construction_county']
   ordering_fields = ['project_comp']

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['firm_id']
    ordering_fields = ['budget']

class ArchitectViewSet(ModelViewSet):
    queryset = Architect.objects.select_related('firm').prefetch_related('project').all()
    serializer_class = ArchitectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['firm_id']
    search_fields = ['computer', 'firm__firm_name', 'firm__country']
    ordering_fields = ['birth_date']
    


        

        