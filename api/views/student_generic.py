from rest_framework import generics
from students.models import Student
from api.serializers import StudentSerializer




class Students(generics.ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    Lookup_field = 'pk'