from django.contrib import admin

from apps.product.models import Product, Brand, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin.
    """
    list_display = (
        'product_name',
        'description',
        'is_digital',
        'category',
        'brand',
        'is_active',
    )
    list_filter = ('category__category_name', 'brand__brand_name', 'is_active')
    search_fields = ('product_name', 'brand__brand_name', 'category__category_name')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Brand model admin.
    """
    list_display = ('brand_name', 'products_count')
    search_fields = ('brand_name',)

    def products_count(self, obj):
        return Product.objects.filter(brand=obj).count()

    products_count.short_description = 'Products'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category model admin.
    """
    list_display = ('category_name', 'parent', 'products_count')
    search_fields = ('category_name', 'parent__category_name')
    list_filter = ('parent',)

    def products_count(self, obj):
        return Product.objects.filter(category=obj).count()

    products_count.short_description = 'Products'
