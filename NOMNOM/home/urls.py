from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, rate_restaurant, PostCreateItemView, PostListItems, favorites
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name ='home'),
    path('add-to-favorites/<int:item_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('favorites/', favorites, name = 'favorites'),
    path('top_menu_items', PostListItems.as_view(), name ='top-menu-items'),
    path('restaurant/<int:pk>/', PostDetailView.as_view(), name ='restaurant-detail'),
    path('restaurant/new/', PostCreateView.as_view(), name ='restaurant-create'),
    path('restaurant/new-item', PostCreateItemView.as_view(), name ='item-create'),
    path('restaurant/<int:pk>/update', PostUpdateView.as_view(), name ='restaurant-update'),
    path('restaurant/<int:pk>/delete', PostDeleteView.as_view(), name ='restaurant-delete'),
    path('restaurant/<int:pk>/rate/', rate_restaurant, name='rate-restaurant'),
    path('item/<int:pk>/rate/', views.rate_item, name='rate-item'),
    path('about/', views.about, name='home-about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)