from django.shortcuts import render, redirect
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
