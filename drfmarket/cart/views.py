from django.shortcuts import render
from rest_framework import generics ,viewsets , status
from main.serializers import *
from rest_framework.views import Response,APIView
from django.forms import model_to_dict
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,IsAuthenticated
from main.permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin,DestroyModelMixin
from .serializers import *


from .models import  *

class CartUserAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Cart.objects.filter(user_cart=self.request.user)


    serializer_class = CartSerializer




class CartAllViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()

    serializer_class = CartSerializer

# class AddToCartView(APIView):
#     def post(self, request):
#         cart = Cart.objects.get(user=request.user)
#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             product_id = serializer.validated_data['product']
#             quantity = serializer.validated_data.get('quantity', 1)
#             product = Articles.objects.get(pk=product_id)
#             cart_item, created = CartItem.objects.get_or_create(product=product, defaults={'quantity': quantity})
#             if not created:
#                 cart_item.quantity += quantity
#                 cart_item.save()
#             cart.items.add(cart_item)
#             return Response({'success': True})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)