from django.contrib import admin
from .models import Product, Category, Promotion


class PromotionAdmin(admin.ModelAdmin):
    list_display = ['proms']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'edited_at']
    list_filter = ['available', 'created_at', 'edited_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Promotion, PromotionAdmin)

