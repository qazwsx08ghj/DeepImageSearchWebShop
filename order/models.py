from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
from datetime import datetime
# Create your models here.


User = get_user_model()


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")

    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods")
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        verbose_name = 'shopping cart'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return str("goods:"+self.goods.name + "Quantity:" + str(self.quantity) + " create cart in:" + str(self.add_time))


class OrderDetail(models.Model):
    status = (
        ("success", "成功"),
        ("close", "結束"),
        ("create", "建立"),
        ("finished", "完成交易"),
        ("paying", "待支付"),
    )

    payments = (
        ('creditcard', '信用卡'),
        ('COD', '貨到付款')
    )

    # 訂單狀態
    OStatus = models.CharField(choices=status, default="", max_length=200, verbose_name="order status")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="pay time for this order")

    # 購買人資訊
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='buyer')
    shipping = models.CharField(max_length=200, default='XXX', null=True, blank=True, verbose_name='ship')
    cardInfo = models.CharField(max_length=200, null=True, blank=True)

    # 付款方式
    payment = models.CharField(choices=payments, default="COD", max_length=200)

    # 價錢
    price = models.IntegerField(default=0, verbose_name='price of order')

    # 收貨人資訊
    BAddress = models.CharField(default="", max_length=200, verbose_name='shipping place')
    receiver = models.CharField(default=buyer.name, max_length=200, verbose_name='receiver')
    RPhoneNum = models.CharField(default='', max_length=200)

    add_time = models.DateTimeField("create time", default=datetime.now)

    class Meta:
        verbose_name = "Order Detail"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str("customer:"+self.buyer.name + " create order in:" + self.add_time)


class OrderGoods(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE, verbose_name='order Detail', related_name="Goods")
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='goods')
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity of goods')

    add_time = models.DateTimeField("create time", default=datetime.now)

    class Meta:
        verbose_name = "Goods in order"
        verbose_name_plural = verbose_name



