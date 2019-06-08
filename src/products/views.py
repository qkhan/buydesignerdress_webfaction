from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.http import Http404
from items.models import Item, Brand, Category, Prospect, Color, ProductType, Category
#from e_carts.models import Cart
from s_carts.models import Cart
from django.utils import timezone
from itertools import chain
from django.forms.models import model_to_dict
from django.db.models import Q
import pdb
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django import template

register = template.Library()

class ProductListView(ListView):
    template_name = "products/list.html"

    def get_success_url(self):
        return reverse("product_list")


    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print("CONTEXT")
        print(context)
        #color = Option.objects.filter(optionGroupId='1')
        #print ("METHOD : ", self.request.method)
        for key in self.request.GET:
            #print("KEY: ",key)
            value = self.request.GET[key]
            #print("VAL: ",value)

        if self.request.method == 'GET':
            values_from_color_checkbox = self.request.GET.getlist('color_checkbox_val')
            values_from_brand_checkbox = self.request.GET.getlist('brand_checkbox_val')
            #print ("Values: ", values_from_color_checkbox)

        # color_checkbox_val = self.request.GET["color_checkbox_val"]
        ##print ("color_checkbox_val", color_checkbox_val)
        # context['color_list'] = color
        # context['size_list'] = size
        # context['brand_list'] = brands
        # context['prospect_list'] = prospects
        # context['category_list'] = categories
        #print ("ARGS: ", self.kwargs)
        prospect_type = self.kwargs.get('prospect_type')
        category_type = self.kwargs.get('category_type')
        # color = Color.objects.values()
        # length_color = len(col)

        # color = Color.objects.values_list()
        color = Color.objects.all()
        self.get_color_list(values_from_color_checkbox, color)
        # for key in color_dict:
        #    #print ("KEY:", key)

        #[<Color: red>, <Color: blue>, <Color: green>, <Color: pink>, <Color: purple>, <Color: Yellow>, <Color: Brown>]
        #print(color.__dict__['_result_cache'][0])
        #size = Size.objects.all()
        brands = Brand.objects.all()
        self.get_brand_list(values_from_brand_checkbox, brands)
        prospects = Prospect.objects.all()
        categories = Category.objects.all()
        product_types = ProductType.objects.all()
        clothing_category = Category.objects.filter(productType__productType='Clothing')
        shoes_category = Category.objects.filter(productType__productType='Shoes')
        accessories_category = Category.objects.filter(productType__productType='Accessories')
        featured_category = Category.objects.featured()
        look_and_trends_category = Category.objects.lookAndTrend()
        prospect_list = Prospect.objects.all()
        prospectID = Prospect.objects.get(prospect=prospect_type)
        print ("Prospect ID: ", prospect_type)
        categoryID = Category.objects.get(categoryName = category_type) 
        for pros in prospect_list: 
            print("Prospect: {0} =-= {1}".format(pros.id, pros))

        #colorID = color_dict[]
        # color_id_list = []
        # for col_name in values_from_color_checkbox:
        #    #print ("Col Name: {} -- {}".format(col_name, color_dict[col_name]))
        #     color_id_list.append(str(color_dict[col_name]))

        #color_id_list = color_id_list.rstrip(",")
       #print ("COL LIST", self.color_id_list)
       #print ("categoryID: ", categoryID.id)

        if self.color_id_list and self.brand_id_list:
            item_list = Item.objects.filter(categoryID=categoryID, prospectID=prospectID, color__in=self.color_id_list, brand__in=self.brand_id_list)
        elif self.color_id_list:
            item_list = Item.objects.filter(categoryID=categoryID, prospectID=prospectID, color__in=self.color_id_list)
        elif self.brand_id_list:
            item_list = Item.objects.filter(categoryID=categoryID, prospectID=prospectID, brandID__in=self.brand_id_list)
        else:
            item_list = Item.objects.filter(categoryID=categoryID, prospectID=prospectID)
        # for item in item_list:
        #    #print('ID: {} Name: {}'.format(item.category_set.pk, item.category_set.categoryName))
        #print("ITEMS: ", item_list)
        
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        logger.info("CART OBJECT : PRODUCT LIST: {}".format(cart_obj))
        #print ("NEW OBJECT: PRODUCT LIST: ", new_obj)
        logger.info("CART OBJECT LIST: {}".format(cart_obj.products.all()))
        #context['cart'] = cart_obj

        context = {
            "color_list": color,
            "brand_list": brands,
            "content": "This is content for the home page",
            "prospect_list": prospects,
            "category_list": categories,
            "product_types": product_types,
            "clothing_category": clothing_category,
            "shoes_category": shoes_category,
            "accessories_category": accessories_category,
            "featured_category": featured_category,
            "look_and_trends_category": look_and_trends_category,
            "prospect_list": prospect_list,
            "item_list": item_list,
            "prospect_type": prospect_type,
            "category_type": category_type,
            "values_from_color_checkbox": values_from_color_checkbox,
            "values_from_brand_checkbox": values_from_brand_checkbox,
            "cart": cart_obj,
            #"color_checkbox_val": color_checkbox_val
        }

        #print("QK")
        #print(context)
        return context


    def get_brand_list(self, values_from_brand_checkbox, brands):
        brand_dict = {}
        for col in brands:
           #print ("COl ID: {} --  NAME: {}".format(col.id, col.brandName))
            brand_dict[col.brandName] = col.id

        self.brand_id_list = []
        for col_name in values_from_brand_checkbox:
           #print ("Col Name: {} -- {}".format(col_name, brand_dict[col_name]))
            self.brand_id_list.append(str(brand_dict[col_name]))


    def get_color_list(self, values_from_color_checkbox, color):
        color_dict = {}
        for col in color:
             #print ("COl ID: {} --  NAME: {}".format(col.id, col.color_name))
             color_dict[col.color_name] = col.id

        self.color_id_list = []
        for col_name in values_from_color_checkbox:
           #print ("Col Name: {} -- {}".format(col_name, color_dict[col_name]))
            self.color_id_list.append(str(color_dict[col_name]))


    def get_queryset(self, *args, **kwargs):
        request = self.request

        # self.id, self.optionName, self.optionGroupId
        #color = Option.objects.filter(optionGroupId='1')
        color = Color.objects.all()
        #pdb.set_trace()
        #print("Color:", color)
        #size = Option.objects.filter(optionGroupId='2')
        #print("Size:", size)

        #print("Brands:", brands)
        #categories = Category.objects.all()
        #print("Categories:", categories)
        # categories = Category.objects.all()
        items = Item.objects.all()
        #results = chain(items, color, size, brands, categories)
        return Item.objects.all()
        #return results


class ProductDetailSlugView(DetailView):
    queryset = Item.objects.all()
    template_name = "products/detail.html"


    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
       #print ("METHOD : ", self.request.method)
        for key in self.request.GET:
           #print("KEY: ",key)
            value = self.request.GET[key]
           #print("VAL: ",value)

        # if self.request.method == 'GET':
        #     values_from_color_checkbox = self.request.GET.getlist('color_checkbox_val')
        #     values_from_brand_checkbox = self.request.GET.getlist('brand_checkbox_val')
        #    #print ("Values: ", values_from_color_checkbox)

        color = Color.objects.all()
        brands = Brand.objects.all()
        prospects = Prospect.objects.all()
        categories = Category.objects.all()
        product_types = ProductType.objects.all()
        clothing_category = Category.objects.filter(productType__productType='Clothing')
        shoes_category = Category.objects.filter(productType__productType='Shoes')
        accessories_category = Category.objects.filter(productType__productType='Accessories')
        featured_category = Category.objects.featured()
        look_and_trends_category = Category.objects.lookAndTrend()
        prospect_list = Prospect.objects.all()

        #request = self.request
        #GET parameters from URL   
        slug = self.kwargs.get('slug')
        prospect_type = self.kwargs.get('prospect_type')
        category_type = self.kwargs.get('category_type')
       #print ("Prospect Type:", prospect_type)
       #print ("Category Type:", category_type)
        try:
            instance = Item.objects.get(slug=slug, active=True)
        except Item.DoesNotExist:
            raise Http404("Not Found")
        except Item.MultipleObjectsReturned:
            qs = Item.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Issue accessing the web page")

        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        logger.info("CART OBJECT : PRODUCT LIST: {}".format(cart_obj))
        #instance.colorQK = "red"
       #print ("Instance: ", instance)
        context = {
            "color_list": color,
            "brand_list": brands,
            "object": instance,
            "content": "This is content for the home page",
            "prospect_list": prospects,
            "category_list": categories,
            "product_types": product_types,
            "clothing_category": clothing_category,
            "shoes_category": shoes_category,
            "accessories_category": accessories_category,
            "featured_category": featured_category,
            "look_and_trends_category": look_and_trends_category,
            "prospect_list": prospect_list,
            "prospect_type": prospect_type,
            "category_type": category_type,
            "cart"         : cart_obj,
        }

        return context
