from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket

from store.models import Product


# Create your views here.

def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product, product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty, 'a': basket.a()})
        return response
