from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Restaurant, RestaurantRating
from .models import Item, ItemRating, FavoriteItems
from django.utils.decorators import method_decorator
from .forms import RestaurantRatingForm, ItemRatingForm

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

class PostListItems(ListView):
      model = Item
      template_name = 'home/menu_items.html'
      context_object_name = 'items'
      ordering = ['-Rating']
      paginate_by = 10

class PriceView(ListView):
    context_object_name = 'items'    
    template_name = 'home/price_menu_items.html'
    queryset = Item.objects.filter(Price__gt=5)

class CaloriesView(ListView):
    context_object_name = 'items'    
    template_name = 'home/price_menu_items.html'
    queryset = Item.objects.filter(Calories__gt=500)

class PostDetailView(DetailView):
      model = Restaurant

@method_decorator(staff_member_required, name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
      model = Restaurant
      fields = ['Name', 'Description', 'image']

@method_decorator(staff_member_required, name='dispatch')
class PostCreateItemView(LoginRequiredMixin, CreateView):
      model = Item
      fields = ['RestaurantID','Name', 'Description', 'Price', 'Calories', 'image']

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
    user = request.user
    if request.method == 'POST':
        form = RestaurantRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            # Check if user has already rated this restaurant
            existing_rating = RestaurantRating.objects.filter(user=user, restaurant=restaurant).first()
            if existing_rating:
                existing_rating.rating = rating
                existing_rating.save()
            else:
                rating_obj = RestaurantRating(user=user, rating=rating, restaurant=restaurant)
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
    context = {'form': form, 'restaurant': restaurant}
    return render(request, 'home/rate_restaurant.html', context)



from django.urls import reverse

@login_required
def rate_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    restaurant = item.RestaurantID
    user = request.user
    if request.method == 'POST':
        form = ItemRatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            # Check if user has already rated this item
            existing_rating = ItemRating.objects.filter(user=user, item=item).first()
            if existing_rating:
                existing_rating.rating = rating
                existing_rating.save()
            else:
                rating_obj = ItemRating(user=user, rating=rating, item=item)
                rating_obj.save()
            # Update item rating and number of ratings
            item_ratings = ItemRating.objects.filter(item=item)
            num_ratings = len(item_ratings)
            avg_rating = sum(rating.rating for rating in item_ratings) / num_ratings if num_ratings > 0 else 0
            item.Rating = avg_rating
            item.NumRatings = num_ratings
            item.save()
            return redirect(reverse('restaurant-detail', kwargs={'pk': restaurant.pk}))
    else:
        form = ItemRatingForm()
    context = {'form': form, 'item': item}
    return render(request, 'home/rate_item.html', context)
@login_required
def favorites(request):
      return render(request, 'home/favorites.html')

@login_required
def add_to_favorites(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    user = request.user
    favorite_item = FavoriteItems(user=user, item=item)
    favorite_item.save()
    return render(request, 'home/favorites.html')

def about(request):
        return render(request, 'home/about.html', {'title': 'About'})