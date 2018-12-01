
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .views import ItemDetailView,ItemListView,ItemCreateView,ItemUpdateView,ItemDeleteView

urlpatterns = [
    path('new', ItemCreateView.as_view(), name='item_create'),
    path('<slug:slug>/delete', ItemDeleteView.as_view(), name='item_delete'),
    path('<slug:slug>/update', ItemUpdateView.as_view(), name='item_update'),
    path('<slug:slug>', ItemDetailView.as_view(), name='item_detail'),
    path('', ItemListView.as_view(), name='item_list'),
 ]
