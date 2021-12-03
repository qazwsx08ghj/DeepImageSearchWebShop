from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from .serializers import ShoppingCartSerializer, ShopCartDetailSerializer, OrderDetailSerializer,OrderSerializer
from .models import ShoppingCart, OrderGoods, OrderDetail
# Create your views here.


class ShoppingCartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = ShoppingCartSerializer
    lookup_field = "goods_id"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):

        owner = self.queryset.filter(user=self.request.user)
        return owner

    def get_serializer_class(self):

        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShoppingCartSerializer


class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = OrderSerializer

    def get_serializer_class(self):

        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def get_queryset(self):
        return OrderDetail.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order = serializer.save()
        shopcarts = ShoppingCart.objects.filter(user=self.request.user)
        for shopCart in shopcarts:
            order_goods = OrderGoods()
            order_goods.good = shopCart.goods
            order_goods.quantity = shopCart.quantity
            order_goods.order = order
            order_goods.save()
            shopcarts.delete()
            return order
