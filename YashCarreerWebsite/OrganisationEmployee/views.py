from django.shortcuts import render
from django.http import HttpResponse
from OrganisationEmployee.models import Employee
from OrganisationEmployee.forms import EmpForm

# Create your views here.
def home(request):
    return HttpResponse("This is organisation")

def displayemp(request):
    emp = Employee.objects.all()
    return render(request,"employee.html",{"emp":emp})

def EmployForm(request):
    if request.method =="POST":
        fm = EmpForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['EmployeeName']
            sal = fm.cleaned_data['EmployeeSalary']
            addr = fm.cleaned_data['EmployeeAddress']
            pwd = fm.cleaned_data['password']
            E = Employee(EmployeeName = nm,EmployeeSalary = sal, EmployeeAddress= addr,password=pwd)
            E.save()
    else:
        fm = EmpForm()
    return render(request,'EmployeeForm.html',{'form':fm})
        

