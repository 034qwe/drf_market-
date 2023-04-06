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

class CartAllAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartAllViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()

    serializer_class = CartSerializer
