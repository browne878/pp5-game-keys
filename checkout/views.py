from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.models import User
from profiles.models import Address
from games.models import Game
from .models import Order, OrderItem

from .forms import OrderForm, OrderItemForm
from profiles.forms import AddressForm

import stripe


def checkout(request):
    cart = request.session.get('cart', {})


    if cart == {}:  # if cart is empty
        return redirect(reverse('cart'))

    if request.method == 'POST':
        request.session['form_submitted'] = True

        token = request.POST['stripeToken']

        user = get_object_or_404(User, pk=request.user.id)

        address_form_data = {
            'user': user,
            'address_line_1': request.POST['address-line-1'],
            'address_line_2': request.POST['address-line-2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'post_code': request.POST['post-code'],
            'phone_number': request.POST['phone-number']
        }

        order_form_data = {
            'full_name': request.POST['full-name'],
            'email': request.POST['email'],
            'order_total': request.POST['order_total'],
        }

        address_form = AddressForm(address_form_data)
        if address_form.is_valid():
            address = Address.objects.filter(user=user)

            if address:
                address.update(**address_form_data)
            else:
                address_form.save()

            address = Address.objects.get(user=user)

            order_form_data['address'] = address
            order_form = OrderForm(order_form_data)
            if order_form.is_valid():
                order = order_form.save()

                for game_id, quantity in cart.items():
                    if game_id == 'total':
                        continue
                    game = get_object_or_404(Game, pk=game_id)
                    order_item = OrderItem(
                        order=order,
                        game=game,
                        quantity=quantity,
                        total=game.price * quantity
                    )
                    order_item.save()
                    total = cart.get('total')
                    stripe_total = round(total * 100)
                    stripe.api_key = settings.STRIPE_SECRET_KEY

                    try:
                        charge = stripe.Charge.create(
                            amount=stripe_total,
                            currency="gbp",
                            description="Game Keys",
                            source=token,
                        )

                        # If charge successful, redirect to success page
                        if charge.paid:
                            return redirect(reverse(
                                'checkout_success',
                                args=[order.order_number]
                            ))
                    except stripe.error.CardError:
                        print('Card declined')
            else:
                print(order_form.errors.as_data())
        else:
            print(address_form.errors.as_data())

    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    cart = request.session.get('cart', {})
    cart.clear()
    request.session['cart'] = cart
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
