import json
from django.shortcuts import render, redirect
from accounts.forms import UserCreationForm, UserLoginForm, GuestForm
from django.http import JsonResponse
from items.models import Item
from s_orders.models import Order
from addresses.models import Address
from accounts.models import GuestEmail
from billing.models import BillingProfile
from .models import Cart, CartItemDetails
import logging
import math 
import pdb

# Get an instance of a logger
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
# Create your views here.


def cart_detail_api_view(request):
    print("CART_API_VIEW")
    #json_data = json.loads(request.body)
    product_id = request.POST['item_prd']
    qty = request.POST['item_qty']
    print("Product ID: {0} | Qty: {1}".format(product_id, qty))
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_item_obj, new_item_obj = CartItemDetails.objects.new_or_get(cart_obj, product_id, qty)
    product_list = []
    for x in cart_obj.products.all():
        product_id = x.id
        print("PRODUCT ITEM : {0}".format(product_id))
        cartItemDtl = CartItemDetails.objects.get_product(cart_obj, x.id)
        print("cartItemDtl: Product ID: {0} | QUANTITY: {1}".format(cartItemDtl.product_id, cartItemDtl.prd_qty))
        product_list.append({
                        "id":x.id,
                        "url":x.get_absolute_url(),
                        "name": x.name,
                        "price": x.price,
                        "discount": x.discount,
                        "image": x.image1.url,
                        "image_link": x.get_customer_detail_url(),
                        "item_qty": cartItemDtl.prd_qty,
                        "priceMinusDiscount": x.priceMinusDiscount,
                    }) 

    logger.info("Products: {}".format(product_list))
    print("API CART ITEM OBJ - PRODUCT ID: {0} | QUANTITY: {1}".format(cart_item_obj.product_id, cart_item_obj.prd_qty))
    cart_data = {"products": product_list, "subtotal": cart_obj.subtotal, "total": cart_obj.total }
    #cart_data = {"cart": cart_obj, "products": product_list })
    return JsonResponse(cart_data)

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New Cart created')
    return cart_obj

def cart_home(request):
    print("CART_HOME")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_products = cart_obj.products.all()

    #logger.info("CART OBJ : {}".format(cart_obj))
    #cart_obj.item_qty = 2
    product_list = []
    total = 0
    for x in cart_products:
        cartItemDtl = CartItemDetails.objects.get_product(cart_obj, x.id)
        x.priceMinusDiscount = (x.price - x.discount) * cartItemDtl.prd_qty;
        print("cartItemDtl: Product ID: {0} | QUANTITY: {1}".format(cartItemDtl.product_id, cartItemDtl.prd_qty))
        x.save()
        product_list.append( {
                        "id":x.id,
                        "url":x.get_absolute_url(),
                        "name": x.name, 
                        "price": x.price,
                        "discount": x.discount, 
                        "image": x.image1.url,
                        "image_link": x.get_customer_detail_url(),
                        "item_qty": cartItemDtl.prd_qty,
                        "priceMinusDiscount": x.priceMinusDiscount,
                    }) 

        total += x.priceMinusDiscount
    
    logger.info("Products: {}".format(product_list))
    cart_obj.total = total
    cart_obj.save()
    logger.info("Total Price : {}".format(total))
    return render(request, "carts/basket.html", {"cart": cart_obj, "products": product_list })

def cart_update(request):
    print("CART_UPDATE")
    logger.info("Request.POST: {}".format(request.POST))
    logger.info("Request.IS AJAX: {}".format(request.is_ajax()))
    product_id = request.POST.get('product_id')
    remove_id = request.POST.get('remove_id')
    qty = request.POST.get('qty')
    if not qty:
        qty = 1
    if product_id is not None:
        logger.info("Product ID: {}".format(product_id))
        try:
            product_obj = Item.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.info("Show message to user, product is gone?")

            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        cart_item_obj, new_item_obj = CartItemDetails.objects.new_or_get(cart_obj, product_id, qty)
        if qty is not None:
            logger.info("Cart Objects: {}".format(cart_obj))
        if remove_id is not None:
            logger.info("Product Obj Removed: {}".format(product_obj))
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.quantity = qty 
            cart_obj.save()
            cart_obj.products.add(product_obj)
            added = True
        request.session['cart_items'] = cart_obj.products.count()
        if request.is_ajax():
            logger.info("Ajax request: {}".format(cart_obj))
            json_data = {
                "added":added,
                "removed": not added,
                "cartItemCount": cart_obj.products.count(),
                "product_id" : product_id, 
                "remove_id" : remove_id, 
            }
            logger.info("JSON RESPONSE: {}".format(json_data))
            return JsonResponse(json_data)
            #return JsonResponse({"message": "Error 400"}, status = 400)
        else:
            return redirect("cart:home")
         
    return redirect("cart:home")


def cart_remove(request):
    print("REMOVE")
    print(request.POST)
    return redirect("cart:home")
    
    """
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Item.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print("Cart Objects")
        print(cart_obj)
        if product_obj in cart_obj.products.all():
            print("Product Obj: ", product_obj)
            cart_obj.products.remove(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    """



def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    b_address_obj = None
    billing_profile = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    login_form = UserLoginForm(request.POST or None)
    guest_form = GuestForm()
    register_form = UserCreationForm()
    user = request.user
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)

    #address_form = AddressForm()
    #bi#lling_address_form = AddressForm()

    #guest_email_id = request.session.get('guest_email_id')
    #print("guest_email_id")
    #print(guest_email_id)
    #if user.is_authenticated:
        #billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user, email=user.email)
    #elif guest_email_id is not None:
         #guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
         #billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email=guest_email_obj.email)
    #else:
        #pass

    billing_address_id = request.session.get("billing_address_id", None) 
    shipping_address_id = request.session.get("shipping_address_id", None) 
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    print("Request: checkout_home")
    print(billing_profile)
    address_qs = None
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
        b_address_obj, b_address_obj_created = Address.objects.new_or_get(request, billing_profile)

     
    context = {
        "object"            : order_obj,
        "billing_profile"   : billing_profile,
        "login_form"        : login_form,
        "guest_form"        : guest_form,
        "register_form"     : register_form,
        "b_address_obj"     : b_address_obj, 
        "address_qs"        : address_qs,
    }
    print("This is Qaisar Khan")
    print(context)

    return render(request, "carts/checkout1.html", context)


def get_payment_method(request):
    print("Payment Request Post")
    print(request.POST)
    order_id = request.POST.get('order_id')
    order = Order.objects.get(order_id=order_id)
    order.delivery_type = request.POST.get('delivery')
    order.save()
    print("Order")
    print(order)
    return render(request, "carts/checkout3.html", {"object": order})

def get_over_review(request):
    print("Order Review Request Post")
    print(request.POST)
    order_id = request.POST.get('order_id')
    order = Order.objects.get(order_id=order_id)
    order.delivery_type = request.POST.get('delivery')
    order.save()
    print("Order")
    print(order)
    return render(request, "carts/checkout4.html", {"object": order})

def get_custom_order(request):
    print("Custom Order Review Request Post")
    print(request.POST)
    order_id = request.POST.get('order_id')
    order_obj = Order.objects.get(order_id=order_id)
    is_done = order_obj.check_done()
    print("Cart Session")
    print(request.session['cart_id'])
    if is_done:
        order_obj.mark_paid()
        request.session['cart_items'] = 0
        del request.session['cart_id']
        
    return render(request, "carts/customer-order.html", {"object": order_obj})
    
def get_custom_orders(request):
    print("Custom Orders Review Request Post")
    print(request.POST)
    
    return render(request, "carts/customer-orders.html", {})
    
def get_wish_list(request):
    print("Custom Orders Review Request Post")
    print(request.POST)
    return render(request, "carts/customer-wishlist.html", {})
    

def get_account_details(request):
    print("Custom Orders Review Request Post")
    print(request.POST)
    return render(request, "carts/customer-account.html", {})
    
def get_shipping_address(request):
    print("SHipping Request Post")
    print(request.POST)
    cart_obj, cart_created = Cart.objects.new_or_get(request)

    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    s_address_obj = None
    order_obj = None
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

        if request.POST:
            s_address_obj, s_address_obj_created = Address.objects.new_or_get(request, billing_profile)

    print("Shipping Address")
    print(s_address_obj)

    context = {
        "object": order_obj,
        "s_address_obj": s_address_obj,
    }

    return render(request, "carts/checkout2.html", context)




#print(dir(request.session))
#request.session.set_expiry(300) # 5 minutes
# key = request.session.session_key
# #logger.info("SESSION KEY: {}".format(key))
# request.session['cart_id'] = 12
# request.session['user'] = request.user.username
