from .serializers import GoodSerializer, GoodImageSerializer
from .models import Goods, GoodsImage
from rest_framework import mixins, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class ListGoodsViewSet(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    queryset = Goods.objects.all().order_by("id")
    serializer_class = GoodSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('id',)

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.request.query_params.get('id', None)
        obj = get_object_or_404(queryset, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class IndexImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsImage.objects.all().order_by('id')
    serializer_class = GoodImageSerializer

