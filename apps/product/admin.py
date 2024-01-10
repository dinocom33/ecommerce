from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from apps.product.models import Product, Brand, Category, ProductLine, ProductImage


class EditLinkInLine(object):
    def edit(self, instance):
        url = reverse(
            f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change',
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe('<a href="{u}">Edit</a>'.format(u=url))
            return link

        return ''


class ProductImageInLine(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInLine, admin.TabularInline):
    """
    ProductLine inline model admin.
    """
    model = ProductLine
    readonly_fields = ('edit',)
    # extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin.
    """
    inlines = [
        ProductLineInline
    ]
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
    inlines = [
        ProductImageInLine
    ]
    list_display = ('product', 'quantity', 'price')
    list_filter = ('product',)
    search_fields = ('product__product_name',)
