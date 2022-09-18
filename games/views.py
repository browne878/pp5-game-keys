from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Game


def all_games(request):
    """ A view to show all games, including sorting and search queries """

    games = Game.objects.all()
    context = {
        'games': games,
    }

    return render(request, "games/games.html", context)


def game_detail(request, pk):
    """ A view to show individual game details """

    game = get_object_or_404(Game, pk=pk)

    context = {
        'game': game,
    }

    return render(request, "game_detail.html", context)


@login_required
def add_game(request):
    return render(request, "add_game.html")


@login_required
def edit_game(request, pk):
    return render(request, "edit_game.html")


@login_required
def delete_game(request, pk):
    return render(request, "delete_game.html")
