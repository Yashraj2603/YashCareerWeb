from django.shortcuts import redirect, render
from django.http import HttpResponse
from .import forms
from authentication.forms import LoginForm
from authentication.models import Signup 
from django.contrib import messages
# Create your views here.
def login(request):
    return HttpResponse("<h1>This is login page.</h1>")

"""def Signup(request):
    if request.method =="POST":
        fm = forms.AuthenticationForm(request.POST)
        if fm.is_valid():
            print("Form Validation is sucess and printing Data")
            print("Name :",fm.cleaned_data['First_name'])
        else:
            print("Form data is not valid")
    else:
        fm = forms.AuthenticationForm()
    return render(request,'myform.html',{'form':fm})
"""  

def signup(request):
    if request.method == "POST":
        fm = forms.AuthenticationForm(request.POST)
        if fm.is_valid():
            first_name = fm.cleaned_data['First_name']
            last_name = fm.cleaned_data['Last_name']
            email_id = fm.cleaned_data['Email_id']
            username = fm.cleaned_data['username']
            pass1 = fm.cleaned_data['pass1']
            S= Signup(First_name=first_name,Last_name=last_name,Email_id=email_id,pass1=pass1,username=username)
            S.save()
            messages.add_message(request,messages.SUCCESS,"Account creation sucessfull")
            messages.info(request,"Go to login now to acess your account.")
        else:
            messages.info(request, "Record not Inserted, Try again.")
    else:
        fm= forms.AuthenticationForm()
    return render (request , 'myform.html', {'form':fm})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authenticate the user against the Signup model
            user = Signup.objects.filter(username=username, pass1=password).first()
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                # Authentication failed
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

