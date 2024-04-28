from django.db import models

# Create your models here.

class Employee(models.Model):
    EmployeeName = models.TextField(max_length=250)
    EmployeeSalary = models.FloatField()
    EmployeeAddress = models.TextField(max_length=1000)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.EmployeeName


