from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'home.html')
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')




def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Your account has been created successfully! You can now log in.')
                return redirect('login')  # Redirect to login page after successful registration
            except Exception as e:
                messages.error(request, f"Error creating user: {e}")
        else:
            messages.error(request, "Passwords do not match.")
            
    return render(request, 'signup.html')

from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def book_tutor(request):
    return render(request, 'book_tutor.html')

def become_tutor(request):
    return render(request, 'become_tutor.html')