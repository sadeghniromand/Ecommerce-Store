from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='all_product'),
    path('book/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', views.CategoryItemListView.as_view(), name='category_list')
]
