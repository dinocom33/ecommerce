from django.contrib import admin

from apps.product.models import Product, Brand, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
