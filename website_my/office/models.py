from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
# used to link python to databases in this case we are using sqlite
# Create your models here.


class Patient(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(
        default=72, validators=[MinValueValidator(1), MaxValueValidator(200)])

    def __str__(self):
        return f"{self.first_name} ,  {self.last_name}"
