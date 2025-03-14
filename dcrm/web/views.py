from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):

    #Check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in" )
            return redirect('home')
        
        else:
            messages.success(request, "There was an error login in, Please try again")
            return redirect('home')
    else: 
        return render(request, 'home.html', {})






def logout_user(request):
    pass



# Create your views here.
