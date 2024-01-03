from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category model.
    """
    category_name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """
    Brand model.
    """
    brand_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    """
    Product model.
    """
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    category = TreeForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):

        return self.product_name


class ProductLine(models.Model):
    """
    Line of product.
    """
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
