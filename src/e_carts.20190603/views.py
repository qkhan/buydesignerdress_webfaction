from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, Http404
from items.models import Item
from .models import Cart, CartItem

#from accounts.forms import UserCreationForm, UserLoginForm, GuestForm
#from django.http import JsonResponse
#from orders.models import Order
##from addresses.models import Address
#from accounts.models import GuestEmail
#from billing.models import BillingProfile
#from .models import Cart
#import logging
#import math 

class CartView(SingleObjectMixin, View):
    model = Cart
    template_name = "e_carts/basket.html"

    def get_object(self, *args, **kwargs):
        self.request.session.set_expiry(0)
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session["cart_id"] = cart_id
    
        print("Cart ID: ", cart_id)
        cart = Cart.objects.get(id=cart_id)
        if self.request.user.is_authenticated:
            cart.user = self.request.user
            cart.save()
        return cart


    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        print("Request.GET")
        print(request.GET)
        item_id = request.GET.get("product_id")
        delete_item = request.GET.get("delete")
        if item_id:
            item_instance = get_object_or_404(Item, id=item_id)
            qty = int(request.GET.get("qty", 1))
            print("QTY IS: ", qty)

            try:
                if qty < 1:
                    delete_item = True
            except:
                raise Http404

            #cart = Cart.objects.all().first()
            cart_item = CartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
                print("Item: {0} | Qty: {1} | Cart Item: {2}".format(item_id, qty, cart_item))
        context = {
            "object": self.get_object()
        }
        template = self.template_name
        return render(request, template, context)

    def post_old(self, request, *args, **kwargs):
        cart = self.get_object()
        print("Request.post")
        print(request.POST)
        item_id = request.POST.get("product_id")
        delete_item = request.POST.get("delete")
        if delete_item == 'yes':
            delete_item = True

        print("ITEM ID: {0}".format(item_id))

        if item_id:
            item_instance = get_object_or_404(Item, id=item_id)
            qty = int(request.POST.get("qty", 1))
            print("QTY IS: ", qty)
            
            try:
                if qty < 1:
                    delete_item = True
            except:
                raise Http404

            #cart = Cart.objects.all().first()
            cart_item = CartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
                print("Item: {0} | Qty: {1} | Cart Item: {2}".format(item_id, qty, cart_item))
        context = {
            "object": self.get_object()
        }
        template = self.template_name
        return render(request, template, context)
        #return HttpResponseRedirect("/")
