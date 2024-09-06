from django.db import models


class Breed(models.Model):
    size_choices = (
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
    name = models.CharField(max_length=255)
    size = models.CharField(
        max_length=10,
        choices=size_choices,
    )
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    shedding_amount = models.IntegerField()
    exercise_needs = models.IntegerField()

    def __str__(self) -> str:
        return self.name
