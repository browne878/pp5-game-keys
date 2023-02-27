from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    """Form for users to add their delivery address"""

    class Meta:
        model = Address
        fields = "__all__"
