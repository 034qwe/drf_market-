from rest_framework import serializers
from .models import *


class ArticlesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta():
        model = Articles
        fields = '__all__'


class CategoryArticlesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category_Articles
        fields = ('name',)


class CartSerializer(serializers.ModelSerializer):
    products = ArticlesSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'