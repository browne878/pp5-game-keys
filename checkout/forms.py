from django import forms
from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    """ Form for users to add their delivery address """

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(forms.ModelForm):
    """ Form for users to add their delivery address """

    class Meta:
        model = OrderItem
        fields = '__all__'
