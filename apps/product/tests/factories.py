import factory

from apps.product.models import Category, Brand, Product, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    """
    Factory for Category model.
    """
    class Meta:
        model = Category

    category_name = factory.Sequence(lambda n: f'test_category{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    """
    Factory for Brand model.
    """
    class Meta:
        model = Brand

    brand_name = factory.Sequence(lambda n: f'test_brand{n}')


class ProductFactory(factory.django.DjangoModelFactory):
    """
    Factory for Product model.
    """
    class Meta:
        model = Product

    product_name = 'test_product'
    description = 'test_description'
    is_digital = False
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    """
    Factory for ProductLine model.
    """
    class Meta:
        model = ProductLine

    price = 10.00
    sku = '12345'
    quantity = 1
    product = factory.SubFactory(ProductFactory)
    is_active = True
