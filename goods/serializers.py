from rest_framework import serializers
from .models import Goods, GoodsImage


class GoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodSerializer(serializers.ModelSerializer):
    images = GoodImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'


# class ImageSearchSerializer(serializers.Serializer):
#     class Meta:
#         model = GoodsImage
#         fields = ('image',)
