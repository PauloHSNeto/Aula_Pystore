from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from products.models import Product


def cart_detail(request):
    return render(request, "cart/cart_detail.html")