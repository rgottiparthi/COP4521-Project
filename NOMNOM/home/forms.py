from django import forms
from .models import RestaurantRating, ItemRating


class RestaurantRatingForm(forms.ModelForm):
    class Meta:
        model = RestaurantRating
        fields = ['rating']
        labels = {'rating': 'Rate this restaurant (1-5):'}
        widgets = {'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})}

class ItemRatingForm(forms.ModelForm):
    class Meta:
        model = ItemRating
        fields = ['rating']
        labels = {'rating': 'Rate this restaurant (1-5):'}
        widgets = {'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})}