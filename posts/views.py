from django.shortcuts import render


def index(request):
    return render(request, 'posts/index.html')


def history(request):
    return render(request, 'posts/history.html')


def chart(request):
    return render(request, 'posts/chart.html')


def location(request):
    return render(request, 'posts/location.html')


def establish(request):
    return render(request, 'posts/consulting_establish.html')


def market(request):
    return render(request, 'posts/market.html')


def register(request):
    return render(request, 'posts/consulting_register.html')


def find(request):
    return render(request, 'posts/find.html')


def information(request):
    return render(request, 'posts/information.html')


def jv(request):
    return render(request, 'posts/jv.html')


def notice(request):
    return render(request, 'posts/notice.html')


def news(request):
    return render(request, 'posts/news.html')


def reservation(request):
    return render(request, 'posts/reservation.html')


def about(request):
    return render(request, 'posts/about.html')