from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import student_function_base_view
from api.views import employee_function_base_view
from api.views import student_class_base_view
from api.views import employee_class_base_view
from api.views import employee_mixins
from api.views import student_mixins
from api.views import employee_generic
from api.views import student_generic
from api.views import employee_viewset
from api.views import student_viewset


router = DefaultRouter()
router.register('viewsets-employees', employee_viewset.Employees, basename='viewsets-employees')
router.register('model-viewsets-employees', employee_viewset.EmployeeModelViewSet)
router.register('viewsets-students', student_viewset.Students, basename='viewsets-students')
router.register('model-viewsets-students', student_viewset.StudentModelViewSet)

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
    path('generic_employee_detail/<int:pk>/', employee_generic.EmployeeDetail.as_view()),

    path('generic_students/', student_generic.Students.as_view()),
    path('generic_student_detail/<int:pk>/', student_generic.StudentDetail.as_view()),

    path('',include(router.urls))

]
