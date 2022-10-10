from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    stars = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.first_name
