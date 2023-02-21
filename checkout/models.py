import uuid
from django.db import models

from profiles.models import Address
from games.models import Game


class Order(models.Model):
    """ Order model """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def _generate_order_number(self):
        """ Generates a random, unique order number using UUID """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """ Ensure order number is set on save """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    """ Order item model """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='items')
    game = models.ForeignKey(
        Game, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=False, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
