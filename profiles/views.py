from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib.auth.models import User
from .models import Address


def profile(request):
    """ Show the user's profile """

    if request.user.is_authenticated:

        user = get_object_or_404(User, pk=request.user.id)
        address = Address.objects.filter(user=user)

        if address:
            context = {
                'address': address[0]
            }
        else:
            context = {}
    else:
        # redirect to login page
        return redirect(reverse('account_login'))

    return render(request, 'profiles/profiles.html', context)
