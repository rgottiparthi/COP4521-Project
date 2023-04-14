from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name ='home'),
    path('restaurant/<int:pk>/', PostDetailView.as_view(), name ='restaurant-detail'),
    path('restaurant/new/', PostCreateView.as_view(), name ='restaurant-create'),
    path('about/', views.about, name='home-about'),
]