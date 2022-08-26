from rest_framework import serializers
from app_demo.models import country

class CountrySerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = country
        fields = '__all__'