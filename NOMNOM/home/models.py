from django.db import models
from django.contrib.auth.models import User

class Restraunt(models.Model):
    RestrauntID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
    Description=models.CharField(max_length=200)

class Item(models.Model):
    RestrauntID = models.ForeignKey(Restraunt, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100)
    Rating = models.FloatField(default=0)
    NumRatings = models.IntegerField()
    Description=models.CharField(max_length=200)
    Price = models.FloatField()
    Calories = models.IntegerField()