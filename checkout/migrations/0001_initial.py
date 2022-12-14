# Generated by Django 3.2 on 2022-09-24 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20220923_1403'),
        ('games', '0005_remove_game_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.address')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.game')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checkout.order')),
            ],
        ),
    ]
