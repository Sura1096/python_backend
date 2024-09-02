from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(
        max_length=10,
        choices=[
            ('Tiny', 'Tiny'),
            ('Small', 'Small'),
            ('Medium', 'Medium'),
            ('Large', 'Large'),
        ],
    )
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self) -> models.CharField:
        return self.name
