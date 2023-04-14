from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Restaurant(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
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

class Item(models.Model):
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
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