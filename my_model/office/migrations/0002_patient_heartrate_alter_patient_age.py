# Generated by Django 4.0.6 on 2022-08-01 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='heartrate',
            field=models.IntegerField(default=60, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxValueValidator(300)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
