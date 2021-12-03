from rest_framework import serializers
from .models import Auction, WatchList, Bid
from goods.models import Goods
from users.serializers import UserProfileSerializer
from django.contrib.auth import get_user_model
from django.db.models import Max


class AuctionSerializer(serializers.ModelSerializer):
    good = Goods.objects.all()
    latest_price = serializers.IntegerField(read_only=True)
    winner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Auction
        fields = "__all__"


# class WatchListSerializer(serializers.ModelSerializer):
#     users = UserProfileSerializer(many=True)
#     auction = Auction.objects.all()
#
#     class Meta:
#         model = WatchList
#         fields = "__all__"


class BidSerializer(serializers.ModelSerializer):
    bidder = get_user_model().objects.all()
    auction = Auction.objects.all()

    class Meta:
        model = Bid
        fields = ('bidder', 'bid_time', 'auction', 'price')

    # def create(self, validated_data):
    #     auction = validated_data['auction']
    #     price = validated_data['price']
    #     Bids = Bid.objects.filter(auction=auction).aggregate(Max('price'))
    #
    #     if Bids:
    #         if price < Bids.price:
    #             message = {
    #                 "error": 'you can\'t go more lower in this price'
    #             }
    #         else:
    #             Bids.price = price
    #             Bid.bidder = validated_data.request.user
    #             Bids.save()
    #
    #             auction.winner = validated_data.request.user
    #             auction.latest_price = validated_data['price']
    #             auction.save()
    #             message = auction
    #     else:
    #         existed = Auction.objects.create(**validated_data)
    #         message = existed
    #     return message


