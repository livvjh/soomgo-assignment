from rest_framework import serializers

from account.account_serializers import AccountSerializer
from product.models import Product, Purchase


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    parent_category = serializers.CharField(source='category.parent_category.name', default=None)

    class Meta:
        model = Product
        fields = [
            'id',
            'parent_category',
            'category_name',
            'name',
            'price',
            'description',
            'created_at',
            'updated_at',
        ]


class ProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'price',
            'description',
        ]


class PurchasePostSerializer(serializers.ModelSerializer):
    product_id_set = serializers.ListField()
    # todo drf document ref serializer를 통해 validation check

    class Meta:
        model = Purchase
        fields = [
            'product_id_set',
        ]


class PurchaseSerializer(serializers.ModelSerializer):
    user = AccountSerializer()
    category = serializers.CharField(source='product.category.name')
    product_name = serializers.CharField(source='product.name')
    price = serializers.CharField(source='product.price')
    description = serializers.CharField(source='product.description')
    product_created_at = serializers.CharField(source='product.created_at')
    product_updated_at = serializers.CharField(source='product.updated_at')
    purchased_date = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        fields = [
            'user',
            'category',
            'id',
            'product_name',
            'price',
            'description',
            'product_created_at',
            'product_updated_at',
            'purchased_date'
        ]

    def get_purchased_date(self, obj):
        return obj.created_at
