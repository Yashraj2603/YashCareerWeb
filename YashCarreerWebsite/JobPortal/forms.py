from django import forms
from .models import Candidates, Company

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
