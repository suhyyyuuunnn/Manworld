from django.urls import path
from .views import index, history

app_name = "posts"
urlpatterns = [
    path('index/', index, name="index"),
    path('history/', history, name="history"),
]
