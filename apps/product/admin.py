from django.contrib import admin

from apps.product.models import Product, Brand, Category, ProductLine


class ProductLineInline(admin.TabularInline):
    """
    ProductLine inline model admin.
    """
    model = ProductLine
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin.
    """
    inlines = [ProductLineInline]
    list_display = (
        'product_name',
        'is_digital',
        'category',
        'brand',
        'description',
        'is_active',
    )
    list_filter = ('category__category_name', 'brand__brand_name', 'is_active')
    search_fields = ('product_name', 'brand__brand_name', 'category__category_name')
    auto_populate_fields = ('slug',)


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


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    """
    ProductLine model admin.
    """
    list_display = ('product', 'quantity', 'price')
    list_filter = ('product',)
    search_fields = ('product__product_name',)
