from rest_framework import serializers

from .models import Category, Brand, Product, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer.
    """

    class Meta:
        model = Category
        fields = ['category_name']


class BrandSerializer(serializers.ModelSerializer):
    """
    Brand model serializer.
    """

    class Meta:
        model = Brand
        exclude = ['id']


class ProductImageSerializer(serializers.ModelSerializer):
    """
    Product Image model serializer.
    """

    class Meta:
        model = ProductImage
        exclude = ['id', 'product_line']


class ProductLineSerializer(serializers.ModelSerializer):
    """
    ProductLine model serializer.
    """
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            'price',
            'sku',
            'quantity',
            'order',
            'product_image',
        ]


class ProductSerializer(serializers.ModelSerializer):
    """
    Product model serializer.
    """

    brand_name = serializers.CharField(source='brand.brand_name')
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_name',
                  'slug',
                  'description',
                  'is_active',
                  'brand_name',
                  'category_name',
                  'product_line'
                  ]
