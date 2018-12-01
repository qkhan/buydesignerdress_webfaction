from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from items.models import Item
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        logger.info("MODEL Cart ID: {}".format(cart_id))
        qs = self.get_queryset().filter(id=cart_id)
        logger.info("QUERY SET COUNT: {}".format(qs.count()))
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            logger.info("REQUEST USER : {}".format(request.user))

            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                logger.info("CART OBJ USER: {}".format(cart_obj.user))
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            logger.info("NEW CART OBJ ID: {}".format(cart_obj.id))
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj


    def new(self, user=None):
        user_obj = None
        if user is not None:
            logger.info("USER: {}".format(user))
            if user.is_authenticated:
                user_obj = user
                logger.info("User Object: {}".format(user_obj.username))
        return self.model.objects.create(user=user_obj)

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='cart_user')
    products = models.ManyToManyField(Item, blank=True)
    total    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    update   = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)



def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    logger.info("ACTION: {}".format(action))
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price

        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal * 1.1

pre_save.connect(pre_save_cart_receiver, sender=Cart)
