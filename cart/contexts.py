from django.shortcuts import get_object_or_404

from games.models import Game


def cart_contents(request):
    """
    Ensures that the cart contents
    are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    game_count = 0

    for game_id, quantity in cart.items():
        if (game_id == 'total'):
            continue
        game = get_object_or_404(Game, pk=game_id)
        total += quantity * game.price
        game_count += quantity
        cart_items.append(
            {'game_id': game_id, 'quantity': quantity, 'game': game})

    return {'cart_items': cart_items, 'total': total, 'game_count': game_count}
