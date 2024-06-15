from django.contrib.auth import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *
from .forms import FeedbackForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

def design(request):
    return render(request, "design.html")

def mydesign(request):
    return render(request, "mydesign.html")

def signup(request):
    return render(request, "signup.html")


def registration_view(request):
    user_exists = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        phone = request.POST['phone']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'User with this email already exists. Please log in.')
            return render(request, 'login.html')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.info(request, 'Account created Successfully!')
        return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        if user.check_password(password):
            # If username and password match, redirect to admin page
            if username == 'admin@gmail.com' and password == 'admin':
                return render(request, 'adminhomepage.html') # Assuming the URL name for the admin page is 'admin_page'
            else:
                return  render(request, 'index.html')  # Assuming the URL name for the user page is 'user_page'
        else:
            # If password does not match, display a message
            messages.info(request, 'Invalid password. Please try again')
            return render(request, 'login.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')

def details(request):
    return render(request, 'details.html')

def index(request):
    return render(request, 'index.html')
