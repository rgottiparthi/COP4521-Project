from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
    Description=models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Item(models.Model):
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
    Description=models.CharField(max_length=200)
    Price = models.FloatField()
    Calories = models.IntegerField()