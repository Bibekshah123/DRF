from rest_framework import serializers
from api.models import *

class SathiSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sathi
        fields = '__all__'
        
        