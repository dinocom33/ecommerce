from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

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
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
