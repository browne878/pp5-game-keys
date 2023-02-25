from decimal import Decimal
from django import template


register = template.Library()

@register.filter(name='discount')
def discount(value, discount):
    """ Get the discounted price of a game. """
    
    discounted_price = round(Decimal(value) * Decimal(discount), 2)
    
    return discounted_price