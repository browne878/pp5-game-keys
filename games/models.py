from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    """ Video Game Model """

    statuses = (
        ('1', 'In-Stock'),
        ('2', 'Back-Order'),
        ('3', 'Out-Of-Stock'),
    )

    status = models.CharField(max_length=1, choices=statuses, default='1')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1970), MaxValueValidator(2022)],
        null=True, blank=True
    )
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
