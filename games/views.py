from django.shortcuts import render


def all_games(request):
    return render(request, "games.html")


def game_detail(request, pk):
    return render(request, "game_detail.html")


def add_game(request):
    return render(request, "add_game.html")


def edit_game(request, pk):
    return render(request, "edit_game.html")


def delete_game(request, pk):
    return render(request, "delete_game.html")
