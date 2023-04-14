from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

restaurantsList = [
     {
        'RestaurantID' : '0001',
        'Name' : 'McDonald\'s',
        'Rating' : '5',
        'NumRatings' : '1',
        'Description' : 'I\'m lovin it...'
     },
     {
        'RestaurantID' : '0002',
        'Name' : 'Burger King',
        'Rating' : '3',
        'NumRatings' : '1',
        'Description' : 'Have it your way'
     }
]

def home(request):
    context = {
         'restaurants' : restaurantsList
    }
    return render(request, 'home/home.html', context)
def about(request):
        return render(request, 'home/about.html', {'title': 'About'})
def profiles(request):
    return render(request, 'home/profiles.html', {'title': 'Profiles'})