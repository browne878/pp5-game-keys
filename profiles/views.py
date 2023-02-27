from django.shortcuts import render, redirect, reverse, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Address
from checkout.models import Order


@login_required
def profile(request):
    """Show the user's profile"""

    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        address = Address.objects.filter(user=user)
        orders = Order.objects.filter(user=user)

        if address:
            context = {
                "address": address[0],
                "orders": orders,
            }
        else:
            context = {}
    else:
        # redirect to login page
        return redirect(reverse("account_login"))

    return render(request, "profiles/profiles.html", context)


@login_required
def order_details(request, order_number):
    """Show the user's order details"""

    order = get_object_or_404(Order, order_number=order_number)

    context = {"order": order, "address": order.address}

    return render(request, "profiles/order_details.html", context)
