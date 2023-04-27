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





class CustomPasswordResetView(APIView):
    def post(self, request):
        print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        email1 = request.data.get('email')
        user = User.objects.get(email=email1)
        

        # Generate token and uid for password reset
        token = default_token_generator.make_token(user)
        uid = utils.encode_uid(user.pk)

        # Build password reset URL
        current_site = get_current_site(request)
        reset_url = reverse('password_reset_confirm', kwargs={'uid': uid, 'token': token})
        reset_url = f"http://{current_site.domain}{reset_url}"

        # Build email subject and content
        subject = 'Reset your password'
        message = render_to_string('email/password_reset.html', {
            'reset_url': reset_url,
        })

        # Send email
        email = EmailMessage(subject, message, to=[email1])
        email.send()

        return redirect('password_reset_done')

class PasswordResetView(APIView):

    def get(self, request, uid, token):
       post_data = {'uid': uid, 'token': token}
       return Response(post_data)