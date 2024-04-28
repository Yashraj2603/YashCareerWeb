from django import forms
from django.core import validators

class AuthenticationForm(forms.Form):
    First_name = forms.CharField(validators=[validators.MaxLengthValidator(20)],error_messages={'required':"Enter First Name"})
    Last_name = forms.CharField(validators=[validators.MaxLengthValidator(20)],error_messages={'required':"Enter Second Name"})
    Email_id = forms.EmailField(error_messages={'required':"Enter valid Email"})
    username = forms.CharField(label="Username",max_length=40)
    pass1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    pass2 = forms.CharField(label="ConfirmPassword",widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError("Passwords mismatch ,Please type correct password:")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.CharField(label="email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


