from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.product.fields import OrderField


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Category(MPTTModel):
    """
<<<<<<< Updated upstream
    Category model.
=======
    Category
>>>>>>> Stashed changes
    """
    category_name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='category_name', unique=True)

    objects = ActiveQueryset.as_manager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    """
<<<<<<< Updated upstream
    Brand model.
=======
    Brand
>>>>>>> Stashed changes
    """
    brand_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    """
<<<<<<< Updated upstream
    Product model.
=======
    Product
>>>>>>> Stashed changes
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
    slug = AutoSlugField(populate_from='product_name', unique=True)

    objects = ActiveQueryset.as_manager()

    def __str__(self):

        return self.product_name


class ProductLine(models.Model):
    """
<<<<<<< Updated upstream
    Line of product.
    """
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_line'
    )
    is_active = models.BooleanField(default=False)
    order = OrderField(
        unique_for_field='product',
        blank=True
    )

    objects = ActiveQueryset.as_manager()

    def clean(self, exclude=None):
        qs = ProductLine.objects.filter(product=self.product,)
        for obj in qs:
            if obj.id != self.id and obj.order == self.order:
                raise ValidationError('Order must be unique per product.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sku)


class ProductImage(models.Model):
    """
    Product image model.
    """
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default='test.jpg')
    product_line = models.ForeignKey(
        ProductLine,
        on_delete=models.CASCADE,
        related_name='product_image'
    )
    order = OrderField(
        unique_for_field='product_line',
        blank=True
    )

    def clean(self):
        qs = ProductImage.objects.filter(product_line=self.product_line)
        for obj in qs:
            if obj.id != self.id and obj.order == self.order:
                raise ValidationError('Order must be unique per product.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
