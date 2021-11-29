from rest_framework import serializers
from order.models import OrderGoods, OrderDetail, ShoppingCart
from goods.models import Goods
from goods.serializers import GoodSerializer


class ShopCartDetailSerializer(serializers.ModelSerializer):
    goods = GoodSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "quantity")


class ShoppingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    quantity = serializers.IntegerField(
        required=True,
        label='Quantity',
        min_value=1,
        error_messages={
            "min_value": "You can't make quantity lower than 1",
            "required": "You need to select the quantity of goods"
        }
    )

    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())
    
    def create(self, validated_data):
        user = self.context["request"].user
        quantity = validated_data["quantity"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.quantity += quantity
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        instance.quantity = validated_data["quantity"]
        instance.save()
        return instance


class OrderGoodsSerializers(serializers.ModelSerializer):
    good = GoodSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializers(many=True)

    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # no need when create

    OStatus = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    payment = serializers.CharField(read_only=True)

    class Meta:
        model = OrderDetail
        fields = "__all__"
