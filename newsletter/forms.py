from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    """ Form for users to subscribe to the newsletter """

    class Meta:
        model = Subscription
        fields = '__all__'
