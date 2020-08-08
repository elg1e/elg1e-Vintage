from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def view_cart(request):
    """
    View what is inside the cart
    """
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """
    Add items to cart
    """
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('products'))

def adjust_cart(request, id):
    """
    adjust the quantity of cart items
    """
    quantity = 0
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart')) 