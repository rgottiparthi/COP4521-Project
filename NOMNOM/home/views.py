from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Restaurant
from .models import Item
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def home(request):
    context = {
         'restaurants' : Restaurant.objects.all()
    }
    return render(request, 'home/home.html', context)

class PostListView(ListView):
      model = Restaurant
      template_name = 'home/home.html'
      context_object_name = 'restaurants'
      ordering = ['-Rating']

class PostDetailView(DetailView):
      model = Restaurant

@method_decorator(staff_member_required, name='dispatch')
class PostCreateView(CreateView):
      model = Restaurant
      fields = ['Name', 'Description', 'image']

    #   def form_valid(self, form):
    #         form.instance.RestaurantID = self.request.user
    #         return super().form_valid(form)

def about(request):
        return render(request, 'home/about.html', {'title': 'About'})