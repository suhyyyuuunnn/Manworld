from django.urls import path
from .views import index, history, chart, location, notice, news, reservation, about, business, service, test


app_name = "posts"
urlpatterns = [
    path('index/', index, name="index"),
    path('history/', history, name="history"),
    path('chart/', chart, name="chart"),
    path('location/', location, name="location"),
    path('business/', business, name="business"),
    path('service/', service, name="service"),
    path('notice/', notice, name="notice"),
    path('news/', news, name="news"),
    path('reservation/', reservation, name="reservation"),
    path('about/', about, name="about"),
    path('test/', test, name="test"),
]
