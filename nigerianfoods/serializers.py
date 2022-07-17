from csv import field_size_limit
from rest_framework import serializers
from .models import NigerianFood

class NigerianFoodSerializer(serializers.ModelSerializer):
        class Meta:
            model = NigerianFood
            fields = ['id', 'name', 'description']