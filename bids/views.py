from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from products.views import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='products')
def add_bid(request, id):
    """
    how a user bids
    """
    product = get_object_or_404(Product, pk=id)
    bid = int(float(request.POST.get('bid')))

    if bid > product.price:
        """ change Product.price to bid price """
        product.price = bid
        product.highestBidder = request.user.username
        product.save()
        messages.success(request, 'You are now the highest bidder!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.info(request, 'You must bid higher than the current bid')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
