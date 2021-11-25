from .serializers import GoodSerializer, GoodImageSerializer
from .models import Goods, GoodsImage
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ListGoodsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all().order_by("id")
    serializer_class = GoodSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('id',)


class IndexImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsImage.objects.all().order_by('id')
    serializer_class = GoodImageSerializer

