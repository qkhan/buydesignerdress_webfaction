from django.shortcuts import render

from .models import Cart
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
# Create your views here.
def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    cart_obj.total = total
    cart_obj.save()
    logger.info("Total Price : {}".format(total))
    return render(request, "carts/basket.html", {})

#print(request.session)
#print(dir(request.session))
#request.session.session_key
#request.session.set_expiry(300) # 5 minutes
# key = request.session.session_key
# logger.info("SESSION KEY: {}".format(key))
# request.session['cart_id'] = 12
# request.session['user'] = request.user.username
