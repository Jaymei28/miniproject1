from rest_framework import generics
from employees.models import Employee
from api.serializers import EmployeeSerializer

#class Employees(generics.ListAPIView, generics.CreateAPIView):
#   queryset = Employee.objects.all()
#    serializer_class = EmployeeSerializer



class Employees(generics.ListCreateAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    Lookup_field = 'pk'