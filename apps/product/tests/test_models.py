import pytest
from django.core.exceptions import ValidationError

from apps.product.models import Category, Brand, Product, ProductLine, ProductImage

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    """
    Test Category Model
    """

    def test_str_method(self, category_factory):
        x = category_factory()

        assert str(x) == x.category_name


class TestBrandModel:
    """
    Test Brand Model
    """

    def test_str_method(self, brand_factory):
        """
        Test brand model str method
        """
        x = brand_factory()

        assert str(x) == x.brand_name


class TestProductModel:
    """
    Test Product Model
    """

    def test_str_method(self, product_factory):
        """
        Test product model str method
        """
        x = product_factory()

        assert str(x) == 'test_product'


class TestProductLineModel:
    """
    Test ProductLine Model
    """

    def test_str_method(self, product_line_factory):
        """
        Test productline model str method
        """
        obj = product_line_factory(sku='12345')

        assert str(obj) == '12345'

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        """
        Test productline model duplicate order values
        """
        obj = product_factory()
        product_line_factory(order=1, product=obj)

        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()


class TestProductImageModel:
    """
    Test ProductImage Model
    """

    def test_str_method(self, product_image_factory):
        """
        Test product image model str method
        """
        obj = product_image_factory(url='test_image.jpg')

        assert str(obj) == 'test_image.jpg'
