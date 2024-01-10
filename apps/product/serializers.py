from rest_framework import serializers

from .models import Category, Brand, Product, ProductLine


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


class ProductLineSerializer(serializers.ModelSerializer):
    """
    ProductLine model serializer.
    """

    class Meta:
        model = ProductLine
        exclude = ['id', 'is_active', 'product']


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

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['brand_name'] = instance.brand.brand_name
    #     representation['category_name'] = instance.category.category_name
#         return representation
