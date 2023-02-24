from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SubscriptionForm
from .models import Subscription

# Create your views here.
def newsletter(request):
    """ A view to show the newsletter page and handle subscribe """
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('subscribed'))
        else:
            context = {
                'errors': form.errors.as_text().split('*')[-1]
            }
            return render(request, 'newsletter/newsletter.html', context)
    
    return render(request, 'newsletter/newsletter.html')


def subscribed(request):
    """ A view to show the subscribed page """
    return render(request, 'newsletter/subscribed.html')