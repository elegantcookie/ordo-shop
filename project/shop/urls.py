from django.urls import path, re_path

from .views import (
    Index,
    ProductDetail,
    SearchView,
    get_category

)


app_name = 'shop'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalogue/product/<int:id>', ProductDetail.as_view(), name='product_detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('catalogue/category/<int:id>', get_category, name='get_category'),

]