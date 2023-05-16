from rest_framework import serializers
from .models import Cart,Cartitems, CartOrder
from main.serializers import ArticlesSerializer
from main.models import Articles
from django.contrib.auth.models import User
from django.http import HttpResponse

class CartItemSerializer(serializers.ModelSerializer):
    product = ArticlesSerializer(many=False)
    price_total = serializers.SerializerMethodField(method_name='total')

    class Meta:
        model = Cartitems
        fields = ['id','cart','product','quantity','price_total']


    def total(self,cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price






class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    all_price = serializers.SerializerMethodField(method_name='all_total')

    class Meta:
        model = Cart
        fields = ["id",'items','all_price']
    

    def all_total(self,cart:Cart):
        items = cart.items.all()
        return sum([item.quantity * item.product.price for item in items])

class CartUserSerializer(serializers.ModelSerializer):
    # items = CartItemSerializer(many=True)
    product = ArticlesSerializer(many=False)


    class Meta:
        model = Cartitems
        fields = ['id','product','quantity',]



class CartCreateSerializer(serializers.ModelSerializer):
    user_cart = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'


class CartItemsUserAdd(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['product','quantity']
    
    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        cart_obj, created = Cart.objects.get_or_create(user_cart=user)

        cartitem = Cartitems.objects.create(
            **validated_data, 
            cart=cart_obj
        )

        return cartitem


class CartOrderSerializer(serializers.ModelSerializer):
    item_ids = serializers.IntegerField()

    class Meta:
        model = CartOrder
        fields = ['cartorder_date','item_ids']
    

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        cart_obj = Cart.objects.get(user_cart=user)

        owner_obj = User.objects.get(username=user)
        product_obj = Cartitems.objects.filter(cart=cart_obj)


        cartord= CartOrder.objects.create(
            **validated_data, 
            owner=owner_obj,

        )
        # cartord.product1.set(product_obj)

        cart_obj.items.all().delete()


        return cartord