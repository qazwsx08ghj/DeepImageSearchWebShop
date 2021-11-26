from rest_framework import serializers
from .models import Goods, GoodsImage
from django.contrib.auth import get_user_model


class GoodImageSerializer(serializers.ModelSerializer):
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all())

    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Goods
        fields = '__all__'
