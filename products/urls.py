from django.conf.urls import url, include
from .views import all_products, product_info

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^productInfo/(?P<id>\d+)', product_info, name='product_info')
]