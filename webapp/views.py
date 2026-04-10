from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging



def index(request):
    return render(request, 'pages/index.html', context={'title': 'Focus CRM'})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # login directly after signup
            auth_login(request, user)

            messages.success(request, "Account created successfully")
            return redirect('index')
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
            messages.error(request, "Invalid email or password")

    else:
        form = LoginForm()

    context = {'login_form': form, 'title': 'Focus | Login'}

    return render(request, 'pages/login.html', context)



def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successfully")
    return redirect('login')


@login_required(login_url='login')
def delete_account(request):
    user = request.user
    user.delete()
    auth_logout(request)
    messages.success(request, "Account deleted successfully")
    return redirect('signup')


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    print(form)
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
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


@login_required(login_url='login')
def view_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    title = f'Focus | {record.first_name.capitalize() + " " + record.last_name.capitalize()}'
    context = {'record': record, 'title': title}

    return render(request, 'pages/view_record.html', context)


@login_required(login_url='login')
def delete_record(request, record_id):
    if request.method == "POST":
        record = get_object_or_404(Record, id=record_id)
        record.delete()
        messages.add_message(request, messages.SUCCESS, "Customer Deleted Successfully")
    return redirect('dashboard')



@login_required(login_url='login')
def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            message_text = f"{record.first_name.capitalize() + " " + record.last_name.capitalize()} Info Updated Successfully"
            messages.add_message(request, messages.SUCCESS, message_text)
            return redirect('dashboard')
    
    title = f'{"Update " + record.last_name.capitalize() + " Info"}'
    
    context = {
        'form': form,
        'title': title
    }
    
    return render(request, 'pages/update-record.html', context)

logger = logging.getLogger(__name__)
@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Record.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(id__icontains=query))
    except Exception as e:
        logger.error('Error during search %s', e)
        message_text = "Something went wrong, Try Again"
        messages.add_message(request, messages.ERROR, message_text)

    title = f'{"\"" + query + "\"" + " search results"}'
    
    context = {
        'results': results,
        'query': query,
        'title': title
    }

    return render(request, 'pages/search.html', context=context)

def custom_page_not_found(request, exception):
    context = {
        'title': "404 Page Not Found"
    }

    return render(request, 'pages/404.html', status=404, context=context)

# 404 page for test
def test_page_not_found(request):
    context = {
        'title': "404 Page Not Found"
    }
    
    return render(request, 'pages/404.html', context=context)


def contact_us(request):
    context = {
        'title': "Focus | Contact Us"
    }
    
    return render(request, 'pages/contact-us.html', context=context)

def custom_not_found_page(request, exception):
    context = {
        'title': "404 Page Not Found"
    }

    return render(request, 'pages/404.html', status=404, context=context)
