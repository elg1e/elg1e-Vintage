from django.conf.urls import url, include
from .views import add_bid

urlpatterns = [
    url(r'^addBid/(?P<id>\d+)', add_bid, name='add_bid'),
]