from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from .models import Item
# Create your views here.

def home(request):
    context = {
         'restaurants' : Restaurant.objects.all()
    }
    return render(request, 'home/home.html', context)
def about(request):
        return render(request, 'home/about.html', {'title': 'About'})
def profiles(request):
    return render(request, 'home/profiles.html', {'title': 'Profiles'})