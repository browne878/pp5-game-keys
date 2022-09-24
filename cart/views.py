from games.models import Game
from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    get_object_or_404,
    reverse
)


def view_cart(request):
    """ A view that renders the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, game_id):
    """ Add a quantity of the specified game to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    get_object_or_404(Game, pk=game_id)
    cart = request.session.get('cart', {})

    if game_id in list(cart.keys()):
        cart[game_id] += quantity
    else:
        cart[game_id] = cart.get(game_id, quantity)

    request.session['cart'] = cart
    return redirect(redirect_url)


def modify_cart(request, game_id):
    """ Adjust the quantity of the specified game to the specified amount """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    if quantity > 0:
        cart[str(game_id)] = quantity
    else:
        cart.pop(f"{game_id}")

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, game_id):
    """ Remove the item from the shopping cart """
    redirect_url = request.POST.get('redirect_url')

    try:
        cart = request.session.get('cart', {})
        cart.pop(f"{game_id}")
        request.session['cart'] = cart
        return redirect(redirect_url)

    except Exception:
        return HttpResponse(status=500)
