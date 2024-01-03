from rest_framework import serializers

from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    """
    Category model serializer.
    """

    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """
    Brand model serializer.
    """

    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Product model serializer.
    """

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['brand_name'] = instance.brand.brand_name
        representation['category_name'] = instance.category.category_name
        return representation


class ProductLineSerializer(serializers.ModelSerializer):
    """
    ProductLine model serializer.
    """

    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductLine
        fields = '__all__'
