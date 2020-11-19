from django.urls import path

from .views import (
    cart_add,
    cart_detail,
    remove_product,
    add_quantity,
    take_quantity,
    order_redirect,
)

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('addq/<int:product_id>', add_quantity, name='add_quantity'),
    path('remove/<int:product_id>', remove_product, name='remove_product'),
    path('removeq/<int:product_id>', take_quantity, name='take_quantity'),
    path('order_redirect', order_redirect, name='order_redirect')
]
