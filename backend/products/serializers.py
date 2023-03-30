from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price', 
            'sale_price',
            'discount_price',
        ]
    
    def get_discount_price(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return float(obj.price) * 0.9


