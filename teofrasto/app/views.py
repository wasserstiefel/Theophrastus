from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Architect, Firm, Project, Client
from .serializers import ArchitectSerializer, FirmSerializer, ProjectSerializer, ClientSerializer
from rest_framework import status

# Create your views here.

class FirmViewSet(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    def destroy(self, request, *args, **kwargs):
        if Client.objects.filter(firm_id=kwargs['pk']).count() > 0 or Architect.objects.filter(firm_id=kwargs['pk']).count() > 0:
            return Response({'error': 'firm cannot be eliminated because it is associated with another model'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    


class ProjectViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
  

class ArchitectViewSet(ModelViewSet):
    queryset = Architect.objects.select_related('firm').prefetch_related('project').all()
    serializer_class = ArchitectSerializer


        

        