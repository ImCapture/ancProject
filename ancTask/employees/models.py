from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    position = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    objects = models.Manager()


    #переписанная функция для вывода в админке
    def __str__(self):
        return self.name
        # все еще можно вызвать через родительскую реализацию
        # return super().__str__()
