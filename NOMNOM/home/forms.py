from django import forms
from .models import RestaurantRating


class RestaurantRatingForm(forms.ModelForm):
    class Meta:
        model = RestaurantRating
        fields = ['rating']
        labels = {'rating': 'Rate this restaurant (1-5):'}
        widgets = {'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})}