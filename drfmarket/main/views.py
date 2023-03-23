from django.shortcuts import render
from rest_framework import generics ,viewsets
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination


from .models import  *


class ArticlesAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size =  20


class ArticlesApiList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ArticlesAPIPagination


class ShowCategoryApiList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Articles.objects.filter(categ__slug=self.kwargs['cat_slug'],).select_related('categ')
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ArticlesAPIPagination


class CategoryArticlesApiList(generics.ListCreateAPIView):
    queryset = Category_Articles.objects.all()
    serializer_class = CategoryArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)




class ArticlesAPIUpdate(generics.UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Articles.objects.all() 
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)



# class ArticlesViewSet(viewsets.ModelViewSet):
#     # queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer

#     def get_queryset(self):
#         return Articles.objects.all()