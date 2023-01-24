# Create your views here.
from django.shortcuts import render

def home (request):
    return render(request, 'home.html')

def personal(request):
    return render(request, 'personal.html')

def educational(request):
    return render(request, 'educational.html')

def interests(request):
    return render(request, 'interests.html')

def sale(request):
    return render(request, 'sale.html')

def rolemodel(request):
    return render(request, 'rolemodel.html')


