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



    class Meta:
        model = CartOrder
        fields = ['cartorder_date',]
    


    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        cart_owner = Cart.objects.get(user_cart=user)
        product = Cartitems.objects.filter(cart__user_cart=user)


        cartit = Cartitems.objects.filter(id__in=product)

        for obj in cartit:
            obj.order = CartOrder.objects.get_or_create(owner=user)

            obj.save()
            if obj.order:
                obj.cart = None
                obj.save()

        return cartit


class OrderSerializer(serializers.ModelSerializer):
    product = ArticlesSerializer()

    class Meta:
        model = Cartitems
        fields = '__all__'


class OneOrderSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = Cartitems
        fields = '__all__'


    def create(self, validated_data):
        product_id = validated_data['product_id']
        request = self.context.get("request")
        user = request.user

        crt = Cartitems.objects.create(
            cart=None,
            order=CartOrder.objects.get(owner=user),
            product = Articles.objects.get(pk=product_id),
            quantity = 1
        )
        return crt
#всесте мы все на вайбе, мы круто вайбим, и нету кринжа 
