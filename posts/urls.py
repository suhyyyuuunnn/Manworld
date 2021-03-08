from django.urls import path
from .views import index, history, chart, location, establish, market, register, find, information, jv, notice, news, reservation, about


app_name = "posts"
urlpatterns = [
    path('index/', index, name="index"),
    path('history/', history, name="history"),
    path('chart/', chart, name="chart"),
    path('location/', location, name="location"),
    path('establish/', establish, name="establish"),
    path('market/', market, name="market"),
    path('register/', register, name="register"),
    path('find/', find, name="find"),
    path('information/', information, name="information"),
    path('jv/', jv, name="jv"),
    path('notice/', notice, name="notice"),
    path('news/', news, name="news"),
    path('reservation/', reservation, name="reservation"),
    path('about/', about, name="about"),
]
