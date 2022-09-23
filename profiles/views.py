from multiprocessing import context
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Address


def profile(request):
    """ Show the user's profile """

    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user)

        if address:
            context = {
                'address': address
            }
        else:
            context = {}
    else:
        # redirect to login page
        return redirect(reverse('account_login'))

    return render(request, 'profiles/profiles.html', context)
