from django.db import models


# Create your models here.
class Subscription(models.Model):
    """Stores newsletter subscriptions"""

    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,
        unique=True
    )
