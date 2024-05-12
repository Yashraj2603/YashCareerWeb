from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Candidates, Company
from .forms import ApplyForm,CompanyForm
from .forms import *

# Create your views here.
from django.shortcuts import render
from .models import Candidates, Company

def home(request):
    if request.user.is_authenticated:
        # If the user is logged in, filter candidates based on the logged-in user's company name
        candidates = Candidates.objects.filter(company__name=request.user.company.name)
        context = {'candidates': candidates}
        return render(request, 'hr.html', context)
    else:
        # If the user is not logged in, show all companies and render the job seeker page
        companies = Company.objects.all()
        context = {'companies': companies}
        return render(request, 'Jobseeker.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('login')  #
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=UserCreationForm()
        if request.method=='POST':
            Form=UserCreationForm(request.POST)
            if Form.is_valid():
                currUser=Form.save()
                Company.objects.create(user=currUser,name=currUser.username)
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)


def applyPage(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            if request.user.is_authenticated:
                # If the user is authenticated, associate the candidate with their company
                candidate.company = request.user.company
            candidate.save()
            messages.success(request, 'Your application has been submitted successfully!')
            if request.user.is_authenticated:
                return redirect('home')  # If logged in, redirect to home page
            else:
                return redirect('login')  # If not logged in, redirect to login page
        else:
            # If the form is not valid, display error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
    else:
        form = ApplyForm()

    companies = Company.objects.all()
    context = {'form': form, 'companies': companies}
    return render(request, 'apply.html', context)

@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after adding company
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})