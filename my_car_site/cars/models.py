from django.db import models

# Create your models here.


class Car(models.Model):
    # pk by default
    brand = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"car is  {self.brand} {self.year}"
