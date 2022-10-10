# Generated by Django 4.1 on 2022-09-25 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("office", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="heartrate",
            field=models.IntegerField(
                default=72,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(200),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(120),
                ]
            ),
        ),
    ]