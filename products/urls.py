from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern

from .views import home, product_detail, product_list

app_name = 'products'

urlpatterns = [ 
    path('', product_list, name='products_list'),
    path('home/', home, name='home' ),
    path('<slug:category_slug>', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>', product_detail, name='product_detail'),
]