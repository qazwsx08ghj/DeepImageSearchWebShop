from django.db import models
from django.contrib.auth import get_user_model
import datetime
# Create your models here.

User = get_user_model()


class Goods(models.Model):
    # 賣家
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="seller")

    # 簡單內容
    name = models.CharField("goods name", max_length=200, default="")
    length = models.FloatField("fish length", default=0)
    width = models.FloatField("fish width", default=0)

    # 價格
    price = models.IntegerField("goods price", default=0)

    # 簡述
    # 詳述
    brief = models.TextField("brief for goods", max_length=500, null=True, blank=True)
    description = models.TextField("description for goods", max_length=10000, null=True, blank=True)

    # 圖片區
    indexImage = models.ImageField("image for goods index", upload_to="goods/indexImages", null=True, blank=True)
    # 商品新增時間
    addTime = models.DateTimeField("add time", default=datetime.datetime.now)

    # 有空搞
    # favorite = models.IntegerField("like for this goods", default=0)
    # trackingNum = models.IntegerField("tracker number", default=0)

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="goods", related_name="images")
    image = models.ImageField(verbose_name="image", upload_to="goods/images", null=True, blank=True)
    addTime = models.DateTimeField("add time", default=datetime.datetime.now)

    class Meta:
        verbose_name = 'all goods images'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

#
# class TrackingGoods(models.Model):
#     goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="goods")
#     tracker = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="tracking in this goods")

