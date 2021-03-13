from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST


def index(request):
    return render(request, 'posts/index.html')


def history(request):
    return render(request, 'posts/history.html')


def chart(request):
    return render(request, 'posts/chart.html')


def location(request):
    return render(request, 'posts/location.html')


def notice(request):
    return render(request, 'posts/notice.html')


def reservation(request):
    return render(request, 'posts/reservation.html')


def about(request):
    return render(request, 'posts/about.html')


def service(request):
    return render(request, 'posts/service.html')


def business(request):
    return render(request, 'posts/business.html')


def news(request):
    context = {
        'posts': Post.objects.order_by('-created_at')
    }
    return render(request, 'posts/news.html', context)