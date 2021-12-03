from .serializers import GoodSerializer, GoodImageSerializer
from .models import Goods, GoodsImage
from rest_framework import mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# deepImageSearch
# from DeepImageSearch import LoadData, Index, SearchImage
# from DeepImageSearch.DeepImageSearch import FeatureExtractor
# import DeepImageSearch.config as config
# from PIL import Image
# from annoy import AnnoyIndex
# import pandas as pd
# Create your views here.

#
# class ByteStringSearch(SearchImage):
#     def __init__(self):
#         self.image_data = pd.read_pickle(config.image_data_with_features_pkl)
#         self.f = len(self.image_data['features'][0])
#
#     def search_by_vector(self, v, n: int):
#         v = v  # Feature Vector
#         n = n  # number of output
#         u = AnnoyIndex(self.f, 'euclidean')
#         u.load(config.image_features_vectors_ann)
#         index_list = u.get_nns_by_vector(v, n)  # will find the 10 nearest neighbors
#         return dict(zip(index_list, self.image_data.iloc[index_list]['images_paths'].to_list()))
#
#     def get_query_vector(self, byte_string_image):
#         img = Image.open(byte_string_image)
#         fe = FeatureExtractor()
#         query_vector = fe.extract(img)
#         return query_vector
#
#     def get_similar_images(self, byte_string_image, number_of_images: int):
#         query_vector = self.get_query_vector(byte_string_image=byte_string_image)
#         img_dict = self.search_by_vector(query_vector, number_of_images)
#         return img_dict


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
    ordering_fields = ('goods_id',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # images = LoadData().from_folder(['media/goods/images'])
        # Index(images).Start()


class IndexImagesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsImage.objects.all().order_by('id')
    serializer_class = GoodImageSerializer


class SearchImage(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = GoodImageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = GoodsImage.objects.all().order_by("id")

    # def list(self, request, *args, **kwargs):
    #     file = requset.FILES['image']
    #     httpResponse = {"search Response": None}
    #     images = ["media/"+i.image.name for i in self.queryset.all()]
    #     search = ByteStringSearch().get_similar_images(file, 5)
    #
    #     if search:
    #         for k in search:
    #             name = str()
    #             for s in search[k]:
    #                 if j == "\\":
    #                     print(name[::-1])
    #                     break
    #                 else:
    #                     name += s
    #         httpResponse = {"search Response": 'success'}
    #     Image.objects.create(image=file)
    #     httpResponse.update(search)
    #     return Response(httpResponse)





