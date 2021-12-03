from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Goods
import datetime
# Create your models here.


class Auction(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="AuctionItem", related_name='Goods')
    start_time = models.DateTimeField()
    time_ending = models.DateTimeField()
    bidding_times = models.IntegerField(default=0, verbose_name="bids_Time")
    active = models.BinaryField(default=True)
    winner = models.ForeignKey(get_user_model(), related_name='winner', on_delete=models.CASCADE, blank=True, null=True)
    latest_price = models.IntegerField(default=0, verbose_name='latest_price')

    def __str__(self):
        return "Good:" + str(self.good.name) + "ID:" + str(self.good.id)


class WatchList(models.Model):
    users = models.ManyToManyField(get_user_model(), verbose_name="WatchUser")
    auction = models.ManyToManyField(Auction, verbose_name="watch auction")


class Bid(models.Model):
    bidder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='bidder', related_name='users')
    bid_time = models.DateTimeField(verbose_name="add time", auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, verbose_name='bid auction', related_name='auction')
    price = models.IntegerField(default=0, verbose_name="bid price")
