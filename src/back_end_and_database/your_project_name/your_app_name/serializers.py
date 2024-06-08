from rest_framework import serializers
from .models import Product
from .models import Product_info, PurchaseOrder, SalesOrder, Inventory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.product_name', read_only=True)  #critical to connect to the product name

    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_info
        fields = '__all__'
