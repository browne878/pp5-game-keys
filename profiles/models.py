from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    """Stores Users delivery address"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address_line_1 = models.CharField(max_length=80)
    address_line_2 = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=40)
    county = models.CharField(max_length=80)
    country = models.CharField(max_length=40)
    post_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True)
