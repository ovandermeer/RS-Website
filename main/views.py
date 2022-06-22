from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def deities(request):
    return render(request, 'main/deities.html')


def rituals(request):
    return render(request, 'main/rituals.html')

def about(request):
    return render(request, 'main/about.html')

def based(request):
    return render(request, 'main/based.html')
