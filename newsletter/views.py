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
            context = {
                'errors': form.errors.as_text().split('*')[-1]
            }
            return render(request, 'newsletter/newsletter.html', context)
        
    
    return render(request, 'newsletter/newsletter.html')