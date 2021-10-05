from django.urls import path
from .import views

urlpatterns = [
    path('', views.twitterlottery, name='twitterlottery'),
    path('', views.result, name='result'),
]