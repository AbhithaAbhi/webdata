from django.shortcuts import render
from rest_framework import generics
from .models import EmployeePerformance
from .serializers import EmployeePerformanceSerializer
import requests

# Create your views here.
class EmployeePerformanceList(generics.ListCreateAPIView):
    queryset = EmployeePerformance.objects.all()
    serializer_class =EmployeePerformanceSerializer


def chart_page(request):
    try:
        api_url = "http://127.0.0.1:8000/api/employee-performance/"
        response = requests.get(api_url)
        response.raise_for_status()
        chart_data = response.json()

    except requests.exceptions.RequestException as e:
        chart_data = []

    context = {
        'chart_data': chart_data,
    }

    return render(request, 'index.html', context)