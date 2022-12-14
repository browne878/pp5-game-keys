# Generated by Django 3.2 on 2022-09-17 13:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='game',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('1', 'In-Stock'), ('2', 'Back-Order'), ('3', 'Out-Of-Stock')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='game',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1970), django.core.validators.MaxValueValidator(2022)]),
        ),
    ]
