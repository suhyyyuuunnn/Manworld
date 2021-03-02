from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def history(request):
    return render(request, 'posts/history.html')