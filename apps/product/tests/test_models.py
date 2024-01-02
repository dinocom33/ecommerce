import pytest

from apps.product.models import Category, Brand, Product

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    """
    Test Category Model
    """

    def test_str_method(self, category_factory):
        x = category_factory()

        assert str(x) == x.category_name


class TestBrandModel:

    def test_str_method(self, brand_factory):
        x = brand_factory()

        assert str(x) == x.brand_name


class TestProductModel:

    def test_str_method(self, product_factory):
        x = product_factory()

        assert str(x) == 'test_product'
