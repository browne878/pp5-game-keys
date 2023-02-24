from django.shortcuts import render

from .forms import SubscriptionForm

# Create your views here.
def newsletter(request):
    """ A view to show the newsletter page and handle subscribe """
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
            return render(request, 'newsletter/newsletter.html')
        else:
            print(form.errors)
            return render(request, 'newsletter/newsletter.html')
        
    
    return render(request, 'newsletter/newsletter.html')