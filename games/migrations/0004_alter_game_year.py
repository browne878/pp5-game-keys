# Generated by Django 3.2 on 2022-09-18 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
