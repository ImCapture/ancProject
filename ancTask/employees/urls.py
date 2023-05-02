from employees import views
from django.urls import path

urlpatterns = [
    path('employee_hierarchy/', views.employee_hierarchy_view, name='employee_hierarchy_view'),
    path('employee_hierarchy_json/', views.employee_hierarchy_json, name='employee_hierarchy_json'),
]
