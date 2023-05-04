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
    permission_classes = (IsAdminUser)

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
        return Cart.objects.filter(user_cart=user)
    

    def perform_create(self, serializer):
        cart = self.get_queryset().first()

        purchase = serializer.save(cart=cart)


        cart.items.all().delete()
#я залетаю на биток,серега кипиток,дела все на потом ведь я врубаю свой поток 