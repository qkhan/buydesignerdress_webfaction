"""djuser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


#from e_carts.views import cart_detail_api_view
from accounts.views import register,user_login, home, user_logout, login_page, guest_register_view
from .views import home_page, about_page, contact_page, category_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    #path('login/', user_login_djuser, name='login'),
    path('login/', user_login, name='login'),
    path('login_checkout/', login_page, name='login_checkout'),
    path('register/guest', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('cart/', cart_home, name='cart'),
    #path('cart/', include('e_carts.urls', namespace='cart')),
    path('s_cart/', include('s_carts.urls', namespace='cart')),
    path('logout/', user_logout),
    #path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('', home_page, name='home'),
    path('category/', category_page, name='category'),
    path('about/', about_page, name='about'),
    path('items/', include('items.urls')),
    path('products/', include('products.urls')),
    path('search/', include('search.urls', namespace='search')),
    path('contact/', contact_page, name='contact'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
