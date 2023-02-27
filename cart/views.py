from games.models import Game
from django.urls import reverse
from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart/cart.html")


@login_required
def add_to_cart(request, game_id):
    """Add a quantity of the specified game to the cart"""

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    game = get_object_or_404(Game, pk=game_id)
    cart = request.session.get("cart", {})

    if game_id in list(cart.keys()):
        cart[game_id] += quantity

        if "total" in list(cart.keys()):
            cart["total"] = cart["total"] + (float(game.price) * quantity)
        else:
            cart["total"] = float(game.price) * quantity
    else:
        cart[game_id] = cart.get(game_id, quantity)

        if "total" in list(cart.keys()):
            cart["total"] = cart["total"] + (float(game.price) * quantity)
        else:
            cart["total"] = float(game.price) * quantity

    request.session["cart"] = cart
    return redirect(redirect_url)


def modify_cart(request, game_id):
    """Adjust the quantity of the specified game to the specified amount"""
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    redirect_url = request.POST.get("redirect_url")

    if quantity > 0:
        cart[str(game_id)] = quantity
    else:
        cart.pop(f"{game_id}")

    request.session["cart"] = cart

    # recalculate total
    total = 0
    for game_id, quantity in cart.items():
        if game_id != "total":
            game = get_object_or_404(Game, pk=game_id)
            total += float(game.price) * quantity

    cart["total"] = total

    return redirect(redirect_url)


def remove_from_cart(request, game_id):
    """Remove the item from the shopping cart"""
    redirect_url = request.POST.get("redirect_url")

    try:
        cart = request.session.get("cart", {})
        cart.pop(f"{game_id}")
        request.session["cart"] = cart
        # recalculate total
        total = 0
        for game_id, quantity in cart.items():
            if game_id != "total":
                game = get_object_or_404(Game, pk=game_id)
                total += float(game.price) * quantity

        cart["total"] = total

        return redirect(redirect_url)

    except Exception:
        return HttpResponse(status=500)
