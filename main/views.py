from django.shortcuts import render


def index(request):
    """View index page"""
    return render(request, 'index.html')


def contact(request):
    """View contact page"""
    return render(request, 'contact.html')
