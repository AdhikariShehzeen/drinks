

from stack_data import Serializer
from rest_framework import serializers
from . models import Drinks

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Drinks
        field = ['id', 'name', 'description']
        fields = '__all__'
