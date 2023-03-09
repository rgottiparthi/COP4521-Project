from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('profiles/', views.profiles, name='home-profiles'),
    path('restaurants/', views.restaurants, name='home-restaurants'),
]