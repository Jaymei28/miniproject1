from django.urls import path, include
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view
from api.views import employee_class_base_view
from api.views import employee_mixins
from api.views import student_mixins
from api.views import employee_generic


urlpatterns = [
   path('fbv_students/', student_function_base_view.StudentsList),
    path('fbv_student/<int:student_id>/', student_function_base_view.student), 

    path('cbv_students/', student_class_base_view.Students.as_view()),
    path('cbv_student_detail/<int:pk>/', student_class_base_view.StudentDetail.as_view()),

    path('cbv_employees/', employee_class_base_view.Employees.as_view()),
    path('cbv_employee_detail/<int:pk>/', employee_class_base_view.EmployeeDetail.as_view()),

    path('mixins_employees/', employee_mixins.Employees.as_view()),
    path('mixins_employee_detail/<int:pk>/', employee_mixins.EmployeeDetail.as_view()),

    path('mixins_students/', student_mixins.Students.as_view()),
    path('mixins_student_detail/<int:pk>/', student_mixins.StudentDetail.as_view()),

    path('generic_employees/', employee_generic.Employees.as_view()),
    path('generic_employee_detail/<int:pk>/', employee_generic.EmployeeDetail.as_view())
]
