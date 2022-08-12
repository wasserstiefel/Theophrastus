from importlib.metadata import MetadataPathFinder
from rest_framework import serializers
from app.models import Architect, Firm

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Firm
        fields = ['id', 'firm_name', 'phone_number', 'country']
    
class ArchitectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architect
        fields = ['id', 'first_name', 'last_name', 'firm']
            

    firm = FirmSerializer()

    