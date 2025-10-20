from django.urls import path, include
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view
from api.views import employee_class_base_view


urlpatterns = [
   path('fbv_students/', student_function_base_view.StudentsList),
    path('fbv_student/<int:student_id>/', student_function_base_view.student), 

    path('cbv_students/', student_class_base_view.Students.as_view()),
    path('cbv_student_detail/<int:pk>/', student_class_base_view.StudentDetail.as_view()),

    path('cbv_employees/', employee_class_base_view.Employees.as_view()),
    path('cbv_employee_detail/<int:pk>/', employee_class_base_view.EmployeeDetail.as_view())

]
