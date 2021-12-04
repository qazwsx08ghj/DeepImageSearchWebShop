from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from .serializers import BidSerializer, AuctionSerializer
from rest_framework import viewsets
from .models import Auction, Bid
from datetime import datetime
# Create your views here.


class AuctionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    serializer_class = AuctionSerializer
    queryset = Auction.objects.all().filter(active=True)


class BidViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = BidSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        auction=instance.auction
        this_auction = Auction.objects.get(id=auction.id)

        if this_auction.active:
            if this_auction.time_ending <= datetime.now():
                this_auction.active = False
                this_auction.bidding_times += 1
                this_auction.winner = self.request.user
                this_auction.latest_price = self.request.data['latest_price']
                this_auction.save()
                return this_auction
        else:
            return {"reject": "This auction is ended"}




