from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . import models


# Create your views here.


class ProductListView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'store/home.html'


class ProductDetailView(DetailView):
    queryset = models.Product.objects.filter(in_stock=True)
    template_name = 'store/products/product_detail.html'


class CategoryItemListView(ListView):
    template_name = 'store/products/category_item.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(models.Category, slug=self.kwargs['category_slug'])
        query = models.Product.objects.filter(category=category)
        print(query)
        return query
