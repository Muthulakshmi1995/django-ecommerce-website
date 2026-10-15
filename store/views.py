from django.shortcuts import render
from .models import Category, Product

from django.shortcuts import redirect


def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'home.html', {
        'categories': categories,
        'products': products,
        'cart_count': cart_count,
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    cart[product_id] = cart.get(product_id, 0) + 1

    request.session['cart'] = cart
    return redirect('home')
