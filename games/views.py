from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Game
from .forms import GameForm


def all_games(request):
    """ A view to show all games, including sorting and search queries """

    games = Game.objects.all()
    context = {
        'games': games,
    }

    return render(request, "games/games.html", context)


def game_detail(request, game_id):
    """ A view to show individual game details """

    game = get_object_or_404(Game, id=game_id)

    context = {
        'game': game
    }

    return render(request, "games/game_detail.html", context)


@ login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('games')
    else:
        form = GameForm()

    template = 'games/add_game.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@ login_required
def edit_game(request, game_id):

    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_detail', game_id=game.id)
    else:
        form = GameForm(instance=game)

    template = 'games/edit_game.html'
    context = {
        'form': form,
        'game': game,
    }

    return render(request, template, context)


@ login_required
def delete_game(request, pk):
    return render(request, "delete_game.html")
