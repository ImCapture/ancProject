from django.shortcuts import render

# Create your views here.
from .models import Employee
from django.http import JsonResponse


def employee_hierarchy_view(request):
    # Передать данные в шаблон и отобразить его
    return render(request, "employees/sheets/employee_hierarchyBS.html")


def employee_hierarchy_json(request):
    # Извлечь всех работников из базы данных
    employees = Employee.objects.all()

    # Преобразовать данные в формат, необходимый для их отображения
    employees_json = [
        {
            "id": employee.id,
            "text": f"{employee.name} - {employee.position}",

            # Оставил для сравнения по скорости с первым json форматом из библиотеки JStree
            #            "children": list(employee.children.values('id'))

            # Меняем parent_id root работника с Null на # по требованию AJAX JStree
            "parent": employee.parent_id or '#'
        } for employee in employees
    ]
    return JsonResponse(employees_json, safe=False)
