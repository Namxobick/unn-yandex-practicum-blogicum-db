"""Views of pages app."""
from django.shortcuts import render


def about(request):
    """Render about page."""
    return render(request, 'pages/about.html')


def rules(request):
    """Render rules page."""
    return render(request, 'pages/rules.html')
