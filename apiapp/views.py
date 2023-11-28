from django.shortcuts import render
from rest_framework import viewsets
from apiapp.models import Company,Employee
from apiapp.serializers import companySerialized,EmployeeSerializer

# Create your views here.

class CompanyViewsSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=companySerialized

class EmployeeViewsSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer