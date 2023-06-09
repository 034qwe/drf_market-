from django.shortcuts import render
from rest_framework import generics ,viewsets
from .serializers import *
from rest_framework.views import Response
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser,IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from djoser import utils

from .models import  *


#####
#Articles and CategoryArticles CRUD classes
#####
class ArticlesAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size =  20


class ArticlesApiList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ArticlesAPIPagination


class ShowArticlesApiList(generics.ListAPIView):
    def get_queryset(self):
        pk = self.kwargs.get('pk')

        return Articles.objects.filter(pk=pk)
    
    serializer_class = ArticlesSerializer

        
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
    # permission_classes = (IsOwnerOrReadOnly,)


class ArticlesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Articles.objects.all() 
    serializer_class = ArticlesSerializer
    permission_classes = (IsOwnerOrReadOnly,)



class PasswordResetView(APIView):

    def get(self, request, uid, token):
       post_data = {'uid': uid, 'token': token}
       return Response(post_data)