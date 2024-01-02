import factory

from apps.product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    category_name = factory.Sequence(lambda n: f'test_category{n}')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    brand_name = factory.Sequence(lambda n: f'test_brand{n}')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_name = 'test_product'
    description = 'test_description'
    is_digital = False
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
