from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    release_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
