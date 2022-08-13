from rest_framework import serializers
from app.models import Architect, Firm, Project, Client

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Firm
        fields = ['id', 'firm_name', 'phone_number', 'country', 'address']
        
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =  ['id','building_style', 'country_abr', 'construction_address', 'construction_postal', 'building_material', 'project_overview', 'construction_county', 'project_comp', 'contract_number']

class ArchitectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architect
        fields = ['id', 'first_name', 'last_name', 'firm', 'project', 'computer']
    firm = FirmSerializer()
    project = ProjectSerializer(many=True)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Client
        fields = ['client_name', 'firm', 'website', 'project', 'budget']
    firm = FirmSerializer()
    project = ProjectSerializer()

    