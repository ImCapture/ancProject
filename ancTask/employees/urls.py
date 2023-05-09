import django.views.generic
from employees import views
from employees.views import EmployeeHierarchyJson
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='employees/sheets/employee_hierarchyBS.html'), name='employee_hierarchy'),
    path('employee_hierarchy_json/', EmployeeHierarchyJson.as_view(), name='employee_hierarchy_json'),
]
