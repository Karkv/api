from django.contrib import admin
from django.urls import path,include
from apiapp.views import CompanyViewsSet,EmployeeViewsSet
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register(r'companies',CompanyViewsSet)
routers.register(r'Employee',EmployeeViewsSet)

urlpatterns = [
    path('',include(routers.urls))
]
 