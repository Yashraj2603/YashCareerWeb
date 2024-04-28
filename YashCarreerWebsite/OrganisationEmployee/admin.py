from django.contrib import admin
from OrganisationEmployee.models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["EmployeeName","EmployeeSalary","EmployeeAddress","password"]
#admin.site.register(Employee,EmployeeAdmin)