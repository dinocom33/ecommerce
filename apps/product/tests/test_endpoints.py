import factory
import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = '/api/category/'

    def test_category_list(self, category_factory, api_client):
        category_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['category_name'] == 'test_category0'


class TestBrandEndpoints:
    endpoint = '/api/brand/'

    def test_brand_list(self, brand_factory, api_client):
        brand_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['brand_name'] == 'test_brand0'


class TestProductEndpoints:
    endpoint = '/api/product/'

    def test_product_list(self, product_factory, api_client):
        product_factory.create_batch(5)

        response = api_client.get(self.endpoint)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
        assert json.loads(response.content)[0]['product_name'] == 'test_product'
