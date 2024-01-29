from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Recipes(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=255)
    recipe=models.TextField()

    def __str__(self): 
        return self.food_name