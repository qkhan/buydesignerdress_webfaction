from django.conf import settings
import os
import random
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from multiselectfield import MultiSelectField
import re


def get_filename_ext(filepath):
    base_name  = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext    = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "items/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
        )

def upload_location(instance, filename):
    ItemModel = instance.__class__
    try:
        new_filename = ItemModel.objects.order_by("id").last().id + 1
    except:
        new_filename = 1
    name, ext    = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "items/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
        )


class ItemQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class ProductType(models.Model):
    productType = models.CharField(max_length=250)

    def __str__(self):
        return "{0}".format(self.productType)

    class Meta:
        ordering = ["-id" ]


class CategoryQuerySet(models.query.QuerySet):
    def lookAndTrend(self):
        return self.filter(lookAndTrend=True)

    def featured(self):
        return self.filter(featured=True)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def lookAndTrend(self):
        return self.get_queryset().lookAndTrend()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Category(models.Model):
    categoryName = models.CharField(max_length=250)
    productType  = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product_category' )
    lookAndTrend = models.BooleanField(default=False)
    featured     = models.BooleanField(default=False)

    objects = CategoryManager()

    def __str__(self):
        return "{0}".format(self.categoryName)

    class Meta:
        ordering = ["-categoryName" ]


class Brand(models.Model):
    brandName = models.CharField(max_length=250)

    def __str__(self):
        return "{0}".format(self.brandName)

class Prospect(models.Model):
    prospect = models.CharField(max_length=250)

    def __str__(self):
        return "{0}".format(self.prospect)

    class Meta:
        ordering = ["-prospect" ]

class Country(models.Model):
    country = models.CharField(max_length=250)

    def __str__(self):
        return "{0}".format(self.country)

# class Size(models.Model):
#     size_abbr = models.CharField(max_length=250)
#     size_dtl = models.CharField(max_length=250)
#
#     def __str__(self):
#         return "{0}".format(self.size_dtl)

class Color(models.Model):
    color_name = models.CharField(max_length=250)

    def __str__(self):
        return "{0}".format(self.color_name)

# class MaterialAndCare(models.Model):
#     materialAndCareDesc = models.CharField(max_length=500)
#
#     def __str__(self):
#         return "{0}".format(self.materialAndCareDesc)


# class OptionGroup(models.Model):
#     optionGroupName = models.CharField(max_length=200)
#
#     def __str__(self):
#         return "{0}".format(self.optionGroupName)
#
# class Option(models.Model):
#     optionGroupId = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)
#     optionName = models.CharField(max_length=250)
#
#     def __str__(self):
#         return "{0} - {1} - {2}".format(self.id, self.optionName, self.optionGroupId)

SIZE_CHOICES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Xtra Large'),
    ('XXL', 'Xtra Xtra Large'),
)

SIZE_CHOICES = (
    ('NA', 'Not Applicable'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Xtra Large'),
    ('XXL', 'Xtra Xtra Large'),
)


# class Size(models.Model):
#     SIZE_CHOICES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     size = models.CharField(max_length=20,choices=SIZE_CHOICES, null=True, blank=True)
#
#     def __str__(self):
#         return self.size

# Create your models here.
class Item(models.Model):
    categoryID    = models.ForeignKey(Category, on_delete=models.CASCADE)
    brandID    = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='item_brand', null=True, blank=True)
    prospectID = models.ForeignKey(Prospect, on_delete=models.CASCADE, related_name='item_prospect', null=True, blank=True )
    countryID = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='item_country' )
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='item_add', on_delete=models.CASCADE)
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='item_edit', on_delete=models.CASCADE)
    slug        = models.SlugField(blank=True, unique=True)
    sku  = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    size = MultiSelectField(choices=SIZE_CHOICES)
    weight = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    cartDesc = models.CharField(max_length=120, blank=True, null=True)
    shortDesc = models.CharField(max_length=250, blank=True, null=True)
    materialAndCare  = models.TextField(blank=True, null=True)
    #color = MultiSelectField(choices=[ (o.id, str(o.color_name)) for o in Color.objects.all()])
    color = models.ForeignKey(Color ,  on_delete=models.CASCADE, related_name='item_color', null=True, blank=True)
    fitting  = models.TextField(blank=True, null=True)
    longDesc  = models.TextField(blank=True, null=True)
    thumb_image     = models.ImageField(upload_to=upload_location,
                                        null=True,
                                        blank=True,
                                        width_field="width_field",
                                        height_field="height_field")
    image1        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    image2        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    image3        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    image4        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    image5        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    image6        = models.ImageField(upload_to=upload_location,
                                            null=True,
                                            blank=True,
                                            width_field="width_field",
                                            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    stock = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    live  = models.BooleanField(default=False)
    itemLimited = models.BooleanField(default=False)
    location = models.CharField(max_length=250, blank=True, null=True)
    featured     = models.BooleanField(default=False)
    active     = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    objects = ItemManager()

    def __str__(self):
        return "{0} - {1}".format(self.id, self.title)

    def __unicode__(self):
        return "{0} - {1}".format(self.id, self.title)

    def get_customer_detail_url(self):
        #return "/products/{slug}".format(slug=self.slug)
        return reverse("detail", kwargs={"slug": self.slug, "prospect_type": self.prospectID, "category_type": self.categoryID })

    def get_colors(self):
        color_list = Color.objects.all()
        print ("COLOR:", color_list)
        pass

    def get_absolute_url(self):
        #return "/items/{slug}".format(slug=self.slug)
        return reverse("item_detail", kwargs={"slug": self.slug})

    def get_absolute_url_old(self):
        #return "/items/{slug}".format(slug=self.slug)
        return reverse("item_detail", kwargs={"slug": self.slug, "prospect_type": self.prospect_type, "category_type": self.category_type})

    class Meta:
        ordering = ["-timestamp", "-updated"]

def item_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    if instance.longDesc:
        print("DESC:", instance.longDesc)
        #pattern = re.compile('([^\s\w]|_)+')
        pattern = re.compile('^\W+')
        #strippedList = pattern.sub('', value)
        instance.longDesc = re.sub(r'^\W+$', '', instance.longDesc)
        print("AFTER DESC:", instance.longDesc)
pre_save.connect(item_pre_save_receiver, sender=Item)

# class ItemOptions(models.Model):
#     itemId = models.ForeignKey(Item, related_name='item_for_option', on_delete=models.CASCADE)
#     optionID  = models.ForeignKey(Option, related_name='option_for_item', on_delete=models.CASCADE)
#     optionPriceIncrement = models.DecimalField(decimal_places=2, max_digits=20, default=0)
#     optionGroupId = models.ForeignKey(OptionGroup, related_name='group_for_option', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "{0}".format(self.itemId)
