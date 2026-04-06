from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Record



def index(request):
    return render(request, 'pages/index.html', context={'title': 'Focus CRM'})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
    else:
        form = CreateUserForm()
    
    context = {'signup_form': form, 'title': 'Focus | Signup'}

    return render(request, 'pages/signup.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,  username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.add_message(request, messages.SUCCESS, "Successfull login")
                return redirect('index')

    else:
        form = LoginForm()

    context = {'login_form': form, 'title': 'Focus | Login'}

    return render(request, 'pages/login.html', context)



def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    print(form)
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Customer Added Successfully")
            messages.add_message(request, messages.SUCCESS, "Customer Added Successfully")
            return redirect('dashboard')
    else:
        form = CreateRecordForm()
    
    context = {'createRecordForm': form, 'title': 'Focus | New Customer'}

    return render(request, 'pages/create-record.html', context)


@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    context = {'records': records, 'title': 'Focus | Dashboard'}
    return render(request, 'pages/dashboard.html', context)
