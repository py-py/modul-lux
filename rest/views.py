from rest_framework import viewsets

from backend.models import Product, Category
from rest.serializers import *

__all__ = ('ProductViewSet', 'CategoryViewSet',)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.active_objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.active_objects.all()
    serializer_class = CategorySerializer
