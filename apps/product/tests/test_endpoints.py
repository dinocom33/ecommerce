import json
import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:  # pylint: disable=too-few-public-methods
    """
    Category endpoint tests.
    """
    endpoint = '/api/category/'

    def test_category_list(self, category_factory, api_client):
        """
        List all categories test.
        """
        category_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['category_name'] == 'test_category0'


class TestBrandEndpoints:  # pylint: disable=too-few-public-methods
    """
    Brand endpoint tests.
    """
    endpoint = '/api/brand/'

    def test_brand_list(self, brand_factory, api_client):
        """
        List all brands test.
        """
        brand_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['brand_name'] == 'test_brand0'


class TestProductEndpoints:  # pylint: disable=too-few-public-methods
    """
    Product endpoint tests.
    """
    endpoint = '/api/product/'

    def test_product_list(self, product_factory, api_client):
        """
        List all products test.
        """
        product_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['product_name'] == 'test_product'

    def test_return_single_product_by_name(self, product_factory, api_client):
        """
        Return single product by name.
        """
        obj = product_factory(slug='test-product')
        response = api_client.get(f'{self.endpoint}{obj.slug}/')

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_return_products_by_category(self, product_factory, api_client, category_factory):
        """
        Return products by category.
        """

        obj = category_factory(slug='test-category')
        product_factory(category=obj)

        response = api_client.get(f'{self.endpoint}category/{obj.slug}/')

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1
