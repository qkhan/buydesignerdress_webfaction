import os
import random
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


# def get_filename_ext(filepath):
#     base_name  = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext
#
# def upload_image_path(instance, filename):
#     new_filename = random.randint(1, 3910209312)
#     name, ext    = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "products/{new_filename}/{final_filename}".format(
#             new_filename=new_filename,
#             final_filename=final_filename
#         )
#
# def upload_location(instance, filename):
#     ProductModel = instance.__class__
#     print ("QK!:", ProductModel)
#     try:
#         new_filename = ProductModel.objects.order_by("id").last().id + 1
#     except:
#         new_filename = 1
#     name, ext    = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "products/{new_filename}/{final_filename}".format(
#             new_filename=new_filename,
#             final_filename=final_filename
#         )

#
# class ProductQuerySet(models.query.QuerySet):
#     def active(self):
#         return self.filter(active=True)
#
#     def featured(self):
#         return self.filter(featured=True, active=True)
#
# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model, using=self._db)
#
#     def all(self):
#         return self.get_queryset().active()
#
#     def featured(self):
#         return self.get_queryset().featured()
#
#     def get_by_id(self, id):
#         qs = self.get_queryset().filter(id=id)
#         if qs.count() == 1:
#             return qs.first()
#         return None



# class Category(models.Model):
#     categoryName = models.CharField(max_length=250)
#
#     def __str__(self):
#         return "{0}".format(self.categoryName)
#
# # Create your models here.
# class Product(models.Model):
#     slug        = models.SlugField(blank=True, unique=True)
#     productSKU  = models.CharField(max_length=100, blank=True, null=True)
#     productName = models.CharField(max_length=120)
#     productPrice = models.DecimalField(decimal_places=2, max_digits=20, default=0)
#     productWeight = models.DecimalField(decimal_places=2, max_digits=20, default=0)
#     productCartDesc = models.CharField(max_length=120, blank=True, null=True)
#     productShortDesc = models.CharField(max_length=250, blank=True, null=True)
#     productLongDesc  = models.TextField(blank=True, null=True)
#     productThumb     = models.ImageField(upload_to=upload_location,
#                                         null=True,
#                                         blank=True,
#                                         width_field="width_field",
#                                         height_field="height_field")
#     productImage1        = models.ImageField(upload_to=upload_location,
#                                             null=True,
#                                             blank=True,
#                                             width_field="width_field",
#                                             height_field="height_field")
#     productImage2        = models.ImageField(upload_to=upload_location,
#                                             null=True,
#                                             blank=True,
#                                             width_field="width_field",
#                                             height_field="height_field")
#     productImage3        = models.ImageField(upload_to=upload_location,
#                                             null=True,
#                                             blank=True,
#                                             width_field="width_field",
#                                             height_field="height_field")
#     height_field = models.IntegerField(default=0)
#     width_field = models.IntegerField(default=0)
#     productCategoryID    = models.ForeignKey(Category, on_delete=models.CASCADE)
#     productUpdateDate = models.DateTimeField(auto_now=True, auto_now_add=False)
#     productTimestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     productStock = models.DecimalField(decimal_places=2, max_digits=20, default=0)
#     productLive  = models.BooleanField(default=False)
#     ProductLimited = models.BooleanField(default=False)
#     ProductLocation = models.CharField(max_length=250, blank=True, null=True)
#     featured     = models.BooleanField(default=False)
#     active     = models.BooleanField(default=True)
#
#     objects = ProductManager()
#
#     def __str__(self):
#         return "{0} - {1}".format(self.id, self.productName)
#
#     def __unicode__(self):
#         return "{0} - {1}".format(self.id, self.title)
#
#     def get_absolute_url(self):
#         #return "/products/{slug}".format(slug=self.slug)
#         return reverse("detail", kwargs={"slug": self.slug})
#
#     class Meta:
#         ordering = ["-productTimestamp", "-productUpdateDate"]
#
# def product_pre_save_receiver(sender, instance, *args, **kwargs):
#     print("Hello Qaisar", instance.productName)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#
# pre_save.connect(product_pre_save_receiver, sender=Product)
#
#
#
#
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
#         return "{0}".format(self.optionName)
#
#
# class productOptions(models.Model):
#     productId = models.ForeignKey(Product, related_name='product_for_option', on_delete=models.CASCADE)
#     optionID  = models.ForeignKey(Option, related_name='option_for_product', on_delete=models.CASCADE)
#     optionPriceIncrement = models.DecimalField(decimal_places=2, max_digits=20, default=0)
#     optionGroupId = models.ForeignKey(OptionGroup, related_name='group_for_option', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "{0}".format(self.productId)
