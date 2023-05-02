import random
from django_seed import Seed
import os
import django

levels = 11
employees_per_level = 3
total_employees = employees_per_level * (3 ** levels - 1) // 2


def execute():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ancTask.settings')
    django.setup()
    from employees.models import Employee

    seeder = Seed.seeder()

    seeder.add_entity(Employee, total_employees, {
        'name': lambda x: seeder.faker.name(),
        'email': lambda x: seeder.faker.email(),
        'position': lambda x: seeder.faker.job(),
        'date_joined': lambda x: seeder.faker.date_time_this_year(),
    })

    inserted_pks = seeder.execute()
    employees = Employee.objects.exclude(parent=None)

    for employee in employees:
        parent = employee.parent
        siblings = Employee.objects.filter(parent=parent).exclude(id=employee.id)

        if siblings.count() < employees_per_level:
            employee.parent = parent
            employee.save()
        else:
            new_parent = random.choice(siblings)
            employee.parent = new_parent
            employee.save()

if __name__ == '__main__':
    execute()
