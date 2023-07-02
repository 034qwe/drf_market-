from django.shortcuts import render
from rest_framework import generics ,viewsets , status
from main.serializers import *
from rest_framework.views import Response,APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,IsAuthenticated
from main.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,DestroyModelMixin
from .serializers import *
from rest_framework.permissions import IsAuthenticated


from .models import  *

from .tests import send_notification_to_telegram


class CartUserAPIList(generics.ListAPIView):
    def get_queryset(self):

        return Cartitems.objects.filter(cart__user_cart=self.request.user)
        
    serializer_class = CartUserSerializer
    permission_classes = (IsAuthenticated,)
    

class CartUserAPIDestroy(generics.DestroyAPIView):
    def get_queryset(self):
        return Cartitems.objects.filter(cart__user_cart=self.request.user)

    serializer_class =  CartUserSerializer
    permission_classes = (IsAuthenticated)

class CartAllAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser,)

class CartAPICreate(generics.ListCreateAPIView):
    model = Cart
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer


class CartItemsUserApiAdd(generics.CreateAPIView):
    queryset = Cartitems.objects.all()

    serializer_class = CartItemsUserAdd
    permission_classes = (IsAuthenticated,)


class CartOrderAPIView(generics.CreateAPIView):
    serializer_class = CartOrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Cartitems.objects.filter(cart__user_cart=user)
    
class OrderAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        user = self.request.user
        return Cartitems.objects.filter(order__owner=user)


class OneOrderAPIView(generics.CreateAPIView):
    serializer_class = OneOrderSerializer
    def get_queryset(self):
        user = self.request.user
        return Cartitems.objects.filter(order__owner=user)
#я залетаю на биток,серега кипиток,дела все на потом ведь я врубаю свой поток 


class UpdateOrderStatusAPIView(APIView):

    queryset = CartOrder.objects.all()

    def post(self, request):
        user = self.request.user
        order = Cartitems.objects.filter(order__owner=user).first()
        if order:
            order.is_bought = True
            order.save()

            send_notification_to_telegram(chat_id=5512193079)

            return Response(f"Status updated for order {user}. Notification send to user with id {order.user.id}", status=status.HTTP_200_OK)

        else:
            return Response(f"Order with id {user} does not exist in the system.", status=status.HTTP_400_BAD_REQUEST)