import threading

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from games.models import Game
from .models import Subscription


def send_exclusives():
    """ Email all subscribers with the latest exclusive content. """
    
    subscriptions = Subscription.objects.all()
    
    games = get_random_games()
    
    print(games)
    
    for subscription in subscriptions:
        name = subscription.name
        email = subscription.email
        html_message = render_to_string('email/exclusive.html', {'name': name, 'games': games})
        
        send_mail(
            f'Exclusive Content for {name}!',
            strip_tags(html_message),
            settings.DEFAULT_FROM_EMAIL,
            [email],
            html_message=html_message
        )
    
def get_random_games():
    """ Get a random selection of games from the database. """
    
    games = Game.objects.order_by('?')[:1]
    
    return games


def interval_schedule():
    """ Schedule the task to run every 5 minutes. """
    
    send_exclusives()

    threading.Timer(300, interval_schedule).start()