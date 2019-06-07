
from django.contrib import admin
from django.urls import path
from django.conf import settings

#from .views import cart_home, cart_update, cart_remove, checkout_home, get_shipping_address, get_payment_method, get_over_review, get_custom_order, get_custom_orders, get_wish_list, get_account_details
from .views import CartView

app_name = 'e_carts'

urlpatterns = [
    path('', CartView.as_view(), name='home'),
    path('checkout', CartView.as_view(), name='checkout'),
    path('update', CartView.as_view(), name='update'),
    #path('checkout', checkout_home, name='checkout'),
    #path('shipping', get_shipping_address, name='shipping'),
    #path('payment', get_payment_method, name='payment'),
    #path('custom-order', get_custom_order, name='custom-order'),
    #path('orders', get_custom_orders, name='orders'),
    #path('wish', get_wish_list, name='wish'),
    #path('account', get_account_details, name='account'),
    #path('review', get_over_review, name='review'),
    #path('remove', cart_remove, name='remove')
 ]
