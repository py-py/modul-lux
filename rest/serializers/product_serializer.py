from rest_framework import serializers
from rest_framework.reverse import reverse

from backend.models import Product, ProductImage

__all__ = ('ProductSerializer', 'ProductImageSerialzier',)


class ProductImageSerialzier(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('url', )

    def get_url(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.image.url)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerialzier(many=True)
    default_image = serializers.SerializerMethodField()
    url_product_detail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'images', 'default_image', 'url_product_detail', )

    def get_default_image(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.default_image)

    def get_url_product_detail(self, obj):
        return reverse('backend:product-details', kwargs={'id_product': obj.id})