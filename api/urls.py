from django.urls import path, include
from api.views import student_function_base_view


urlpatterns = [
    path('fbw_students/', student_function_base_view.StudentsList),
]
