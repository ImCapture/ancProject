from .views import EmployeeHierarchyJson
from .views import EmployeeListJson
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='employees/sheets/employee_hierarchy.html'), name='employee_hierarchy'),
    path('employee_hierarchy_json/', EmployeeHierarchyJson.as_view(), name='employee_hierarchy_json'),
    path('employee_list_json/', EmployeeListJson.as_view(), name='employee_list_json'),
    path('list/', TemplateView.as_view(template_name='employees/sheets/employee_list.html'), name='employee_list'),
]
