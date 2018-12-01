
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .views import ProductListView, ProductDetailSlugView#, ProductDetailView


urlpatterns = [
    path('<slug:slug>/<prospect_type>/<category_type>/', ProductDetailSlugView.as_view(), name='detail'),
    #path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('<prospect_type>/<category_type>/', ProductListView.as_view(), name='product_list'),
]
