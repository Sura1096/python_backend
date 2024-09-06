from breed_api.models import Breed
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.RESTRICT)
    gender = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
