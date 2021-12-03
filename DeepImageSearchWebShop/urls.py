"""DeepImageSearchWebShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from rest_framework import routers
from users import views as userViews
from goods import views as goodsViews
from order import views as orderViews
from transaction import views as tViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()

router.register(r'users', userViews.UserViewSet, basename='users')
router.register(r'goods', goodsViews.ListGoodsViewSet, basename='goods')
router.register(r'searchImage', goodsViews.SearchImage, basename='searchImage')
router.register(r'indexImage', goodsViews.IndexImagesViewSet, basename='indexImage')
router.register(r'shopCart', orderViews.ShoppingCartViewSet, basename='shopCart')
router.register(r'order', orderViews.OrderViewset, basename='order')
router.register(r'auction', tViews.AuctionViewSet, basename='auction')
router.register(r'bid', tViews.BidViewSet, basename='bid')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='docs')),
    path('login/', TokenObtainPairView.as_view(), name='jwt_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/', include(router.urls)),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),

]
