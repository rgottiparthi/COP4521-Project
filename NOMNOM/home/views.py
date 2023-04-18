from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
class PostCreateView(LoginRequiredMixin, CreateView):
      model = Restaurant
      fields = ['Name', 'Description', 'image']

@method_decorator(staff_member_required, name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model = Restaurant
      fields = ['Name', 'Description', 'image']

      # check if superuser (only superuser can update)
      def test_func(self):
            restaurant = self.get_object()
            if self.request.user.is_superuser:
                  return True
            return False

@method_decorator(staff_member_required, name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
      model = Restaurant
      success_url = '/'
      
      # check if superuser (only superuser can update)
      def test_func(self):
            restaurant = self.get_object()
            if self.request.user.is_superuser:
                  return True
            return False

def about(request):
        return render(request, 'home/about.html', {'title': 'About'})