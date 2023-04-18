from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name ='home'),
    path('restaurant/<int:pk>/', PostDetailView.as_view(), name ='restaurant-detail'),
    path('restaurant/new/', PostCreateView.as_view(), name ='restaurant-create'),
    path('restaurant/<int:pk>/update', PostUpdateView.as_view(), name ='restaurant-update'),
    path('restaurant/<int:pk>/delete', PostDeleteView.as_view(), name ='restaurant-delete'),
    path('about/', views.about, name='home-about'),
]