from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField(default=0)
    Description=models.CharField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='restaurant_pics')

    def __str__(self):
        return self.Name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'pk': self.pk})

class Item(models.Model):
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField(default=0)
    Description=models.CharField(max_length=200)
    Price = models.FloatField()
    Calories = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='item_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class RestaurantRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    restaurant =  models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class ItemRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    item =  models.ForeignKey(Item, on_delete=models.CASCADE)