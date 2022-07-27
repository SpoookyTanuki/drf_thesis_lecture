from rest_framework import serializers

from backend.models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state',)


class ProductSerializer(serializers.ModelSerializer):
    # shop = serializers.StringRelatedField()
    shop = ShopSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'quantity', 'price', 'shop', )
