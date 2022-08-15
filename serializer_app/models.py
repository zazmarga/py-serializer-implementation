from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Car(models.Model):
    manufacturer = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    horse_powers = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(1914), MinValueValidator(1)]
    )
    needs_to_be_fixed = models.BooleanField()
    problem_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"
