from django.urls import path
from employees.views import employee

urlpatterns = [
    path('',employee.index )
]