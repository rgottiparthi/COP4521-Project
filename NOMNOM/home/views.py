from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def restaurants(request):
        return render(request, 'home/restaurant.html')
def profiles(request):
    return render(request, 'home/profiles.html')