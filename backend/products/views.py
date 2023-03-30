from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_api_view = ProductDetailAPIView.as_view()