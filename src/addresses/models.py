from django.db import models

# Create your models here.
from billing.models import BillingProfile
from django.conf import settings
import pdb
User = settings.AUTH_USER_MODEL

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class AddressManager(models.Manager):

    def new_or_get(self, request, billing_profile):
        address_dict = {}
        created = False
        obj = {}
        address_dict = request.POST.dict()
        if 'user' in address_dict: 
            del address_dict['user']
        if 'csrfmiddlewaretoken' in address_dict: 
            del address_dict['csrfmiddlewaretoken']
        print("Qaisar Shipping")
        print(address_dict)
        print ("Billing Profile")
        print (billing_profile)
        if address_dict:                                                #)
            address_dict['billing_profile'] = billing_profile
            obj, created = self.model.objects.update_or_create(address_dict)
            address_type = address_dict['address_type']
            request.session[address_type + "_address_id"] = obj.id
        else:
            try:
                obj = self.model.objects.get(billing_profile=billing_profile)
                print("Object already there")
                print(obj)
            except self.model.DoesNotExist:
                obj = {}
        
        return obj, created


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.CASCADE)
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    firstname = models.CharField(max_length=120)
    lastname  = models.CharField(max_length=120, null=True, blank=True)
    company = models.CharField(max_length=120, null=True, blank=True)
    street = models.CharField(max_length=400, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.CharField(max_length=120, null=True, blank=True)
    state           = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='Australia')
    phone = models.CharField(max_length=120, default='Australia')
    email = models.CharField(max_length=120, default='Australia')

    objects = AddressManager()

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.address_type, self.firstname, self.street, self.city, self.postal_code, self.state, self.country)

    def get_address(self):
        return "{street}<br/>{city}<br/>{state}{postal_code}<br/>{country}".format(
            line1 = self.street,
            city = self.city,
            state = self.state,
            postal_code = self.postal_code,
            country = self.country
        )


