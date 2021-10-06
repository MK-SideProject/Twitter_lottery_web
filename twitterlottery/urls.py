from django.urls import path
from .views import twitterlottery
urlpatterns = [
    path('', twitterlottery, name='twitterlottery'),
   # path('result/', views.result, name='result'),
]