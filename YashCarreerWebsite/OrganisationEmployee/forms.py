from django import forms
from OrganisationEmployee.models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"