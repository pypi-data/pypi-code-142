from django.urls import path

from huscy.appointments.feed import AppointmentFeed
from huscy.appointments.feed import get_feed_url


urlpatterns = [
    path('feed/<str:token>', AppointmentFeed(), name='feed'),
    path('feedurl/', get_feed_url, name='feed-url'),
]
