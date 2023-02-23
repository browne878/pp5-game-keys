from django.shortcuts import render

# Create your views here.
def newsletter(request):
    return render(request, 'newsletter/newsletter.html')