from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


@extend_schema(tags=['Category'])
class CategoryViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing and editing category instances.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        """
        List all categories.
        """
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Brand'])
class BrandViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing and editing brand instances.
    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        """
        List all brands.
        """
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(tags=['Product'])
class ProductViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing and editing product instances.
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        """
        List all products.
        """
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path=r'category/(?P<category>\w+)/all')  # \w+)/all
    def list_product_by_category(self, request, category=None):
        """
        List all products by category.
        """
        serializer = ProductSerializer(self.queryset.filter(category__category_name=category), many=True)
        return Response(serializer.data)
