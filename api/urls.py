from django.urls import path, include
from api.views import student_function_base_view
from api.views import employee_function_base_view


urlpatterns = [
    path('fbv_students/', student_function_base_view.StudentsList),
    path('fbv_student/<int:student_id>/', student_function_base_view.student),

    path('fbv_employees/', employee_function_base_view.EmployeesList),
    path('fbv_employee/<int:employee_id>/', employee_function_base_view.employee)
]
