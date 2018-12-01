from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .forms import ContactForm
from items.models import ProductType, Category, Prospect
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
def home_page(request):
    #logger.info(request.session.get("first_name"))
    product_types = ProductType.objects.all()
    clothing_category = Category.objects.filter(productType__productType='Clothing')
    shoes_category = Category.objects.filter(productType__productType='Shoes')
    accessories_category = Category.objects.filter(productType__productType='Accessories')
    featured_category = Category.objects.featured()
    look_and_trends_category = Category.objects.lookAndTrend()
    prospect_list = Prospect.objects.all()

    context = {
        "title": "Hello World!",
        "content": "This is content for the home page",
        "product_types": product_types,
        "clothing_category": clothing_category,
        "shoes_category": shoes_category,
        "accessories_category": accessories_category,
        "featured_category": featured_category,
        "look_and_trends_category": look_and_trends_category,
        "prospect_list": prospect_list,
    }
    return render(request, 'index.html', context)

def category_page(request):
    context = {
        "title": "Contact Page",
        "content": "This is content for the Contact page",
    }
    return render(request, 'category.html', context)

def about_page(request):
    context = {
        "title": "About Page",
        "content": "This is content for the About page",
    }
    return render(request, 'about.html', context)

def contact_page(request):

    contact_form = ContactForm(request.POST or None)

    context = {
        "title": "Contact",
        "content": "This is content for the Contact page",
        "form" : contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission."})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, 'contact.html', context)
