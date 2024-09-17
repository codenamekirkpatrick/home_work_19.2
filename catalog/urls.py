from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import products_list, product_detail


app_name = CatalogConfig.name

# urlpatterns = [
#     # path("home/", home, name="home"),
#     path('', products_list, name='products_list'),
#     path('contacts/', contacts, name="contacts"),
#     path('product/<int:pk>/', product_detail, name='product_detail')
#     ]



urlpatterns = [
    path("", home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('products', products_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    ]