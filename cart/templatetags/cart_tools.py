from atexit import register
from django import template

register = template.Library()


@register.filter(name='in_list')
def in_list(value, list):
    """ Checks if a value is in a list """

    for item in list:
        print(value)
        if int(item.get('game_id')) == int(value):
            return True

    return False


@register.filter(name='item_quantity')
def item_quantity(value, list):
    """ Gets the quantity of an item in a list """

    for item in list:
        if int(item.get('game_id')) == int(value):
            return item.get('quantity')

    return 0
