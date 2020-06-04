from django.shortcuts import render

# Create your views here.

def add_bid(request, id):
    """
    create a bid
    """
    quantity = int(request.POST.get('quantity'))
    