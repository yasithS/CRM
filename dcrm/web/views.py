from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):

    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully Registered")
            return redirect('home')

    else: 
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # look for records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    
    else:
        messages.success(request, "You must be logged in to view records. ")
        return redirect('home')
    
def delete_user(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        print(customer_record)
        customer_record.delete()
        messages.success(request,  "Customer Record Delete Successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete records.")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New record added")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in first before adding records")

def update_record(request, pk):
    if request.user.is_authenticated:
        currunt_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=currunt_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has been updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Please log in first")
        return redirect('home')
    

    



    





