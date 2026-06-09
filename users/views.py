from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":                
        form = UserCreationForm(request.POST)   #fills the form
        if form.is_valid():                     #checks if everything submitted correctly
            form.save()                         #creates user in database
            return redirect('home')             
    else:                                       #if GET request
        form = UserCreationForm()               
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')