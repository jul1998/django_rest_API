from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
            'sale_price',
            'get_discount',
        ]
