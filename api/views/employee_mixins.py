from ..serializers import EmployeeSerializer
from rest_framework import mixins, generics
from employees.models import Employee


class Employees(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView):                   #mao ni mo handle sa mga crud method

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer       #tawagon ang class nga naa sa serializers.py tapos iyang i serialize      

    def get(self, request):
        return self.list(request)               #list() method ang mo retrieve sa employee data 
    
    def post(self, request):
        return self.create(request)             #create() method ang mo add sa employee data
    

class EmployeeDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, 
                    generics.GenericAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)