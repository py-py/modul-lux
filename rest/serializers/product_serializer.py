from rest_framework import serializers

from backend.models import Product, ProductImage

__all__ = ('ProductSerializer', 'ProductImageSerialzier',)


class ProductImageSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ('product', 'is_default', )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerialzier(many=True)
    default_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'images', 'default_image', )

    def get_default_image(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.default_image)
