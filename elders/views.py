from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    """The home page."""
    return render(request, 'elders/home.html')