from rest_framework import serializers
from .models import *
from versatileimagefield.serializers import VersatileImageFieldSerializer



class CategoryArticlesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category_Articles
        fields = ('name',)


class ArticlesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlesImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )


class ArticlesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = ArticlesImageSerializer(source='articlesimage_set',many=True)

    class Meta():
        model = Articles
        fields = '__all__'
