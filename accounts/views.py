from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name=request.POST.get("first_name", "default value")
        last_name=request.POST.get("last_name", "default value")
        username = request.POST['username']
        email=request.POST.get("email", "default value")
        password=request.POST.get("password", "default value")
        password2=request.POST.get("password2", "default value")

        # check if passwords match
        if password == password2:
            if User.objects.filter(username=username):
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, 
                    email=email, first_name=first_name, last_name=last_name)

                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST.get("username", "default value")
        password=request.POST.get("password", "default value")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Info')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
