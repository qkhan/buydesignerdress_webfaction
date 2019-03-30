
from django.contrib import admin
from django.urls import path
from django.conf import settings

from .views import SearchItemView 

app_name = 'search'

urlpatterns = [
    path('', SearchItemView.as_view(), name='query'),
 ]
