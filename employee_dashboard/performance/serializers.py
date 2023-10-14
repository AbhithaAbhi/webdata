from .models import EmployeePerformance
from rest_framework import serializers

class EmployeePerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmployeePerformance
        fields='__all__'