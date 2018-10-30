from rest_framework import serializers

from backend.models import Category, CategoryImage

__all__ = ('CategorySerializer', 'CategoryImageSerialzier',)


class CategoryImageSerialzier(serializers.ModelSerializer):
    class Meta:
        model = CategoryImage
        exclude = ('category', 'is_default',)


class CategorySerializer(serializers.ModelSerializer):
    images = CategoryImageSerialzier(many=True)
    default_image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'images', 'default_image',)

    def get_default_image(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.default_image)
