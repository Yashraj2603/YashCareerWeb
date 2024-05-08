from django.forms import ModelForm
from .models import *

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"