from django.shortcuts import render
from students.models import Student
from ..serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def StudentsList(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serialize = StudentSerializer (students, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)