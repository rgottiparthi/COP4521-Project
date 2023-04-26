from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Restaurant, RestaurantRating
from .models import Item
from django.utils.decorators import method_decorator
from .forms import RestaurantRatingForm

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
      paginate_by = 10

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

@login_required
def rate_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            rating_obj = RestaurantRating(user=request.user, rating=rating, restaurant=restaurant)
            rating_obj.save()
            # Update restaurant rating and number of ratings
            restaurant_ratings = RestaurantRating.objects.filter(restaurant=restaurant)
            num_ratings = len(restaurant_ratings)
            avg_rating = sum(rating.rating for rating in restaurant_ratings) / num_ratings if num_ratings > 0 else 0
            restaurant.Rating = avg_rating
            restaurant.NumRatings = num_ratings
            restaurant.save()
            return redirect('restaurant-detail', pk=restaurant.pk)
    else:
        form = RestaurantRatingForm()
    return render(request, 'home/rate_restaurant.html', {'form': form})


def about(request):
        return render(request, 'home/about.html', {'title': 'About'})