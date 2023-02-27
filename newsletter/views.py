from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import SubscriptionForm
from .models import Subscription


# Create your views here.
def newsletter(request):
    """A view to show the newsletter page and handle subscribe"""

    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

            name = request.POST["name"]
            email = request.POST["email"]
            html_message = render_to_string("email/subscribed.html")

            send_mail(
                f"Thank you for Subscribing {name}!",
                strip_tags(html_message),
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=html_message,
            )

            return redirect(reverse("subscribed"))
        else:
            context = {"errors": form.errors.as_text().split("*")[-1]}
            return render(request, "newsletter/newsletter.html", context)

    return render(request, "newsletter/newsletter.html")


def subscribed(request):
    """A view to show the subscribed page"""
    return render(request, "newsletter/subscribed.html")
