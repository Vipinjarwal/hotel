
from django.shortcuts import render, redirect
from .forms import Hotel_Form, Customer_Form

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = Hotel_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Hotel_Form
    context = {'form': form}      
    return render(request, 'index.html', context)

 
def indore(request):
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Customer_Form()
    context = {'form': form}  
    return render(request, 'indorehotel.html', context)


def pune(request):
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Customer_Form()
    context = {'form': form} 
    return render(request, 'punehotel.html', context)
    

def mumbai(request):
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Customer_Form()
    context = {'form': form} 
    return render(request, 'mumbaihotel.html', context)

        