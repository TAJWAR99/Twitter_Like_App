from django.urls import path
from tweets.views import *

urlpatterns = [
    path('',home_view),
    path('create-tweet/',tweet_create_view),
    path('tweets/',tweet_list_view),
    path('tweets/<int:tweet_id>',tweet_detail_view),
]
