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



from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from djoser.views import PasswordResetView
from djoser.serializers import PasswordResetSerializer
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.template import loader
from django.urls import reverse
from django.conf import settings
from djoser import utils
from djoser.conf import settings as djoser_settings


class CustomPasswordResetView(PasswordResetView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        context = {
            'email': user.email,
            'domain': request.META['HTTP_HOST'],
            'site_name': 'Your Site',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'http',
        }
        self.send_reset_password_email(context)
        return Response({'detail': _('Password reset e-mail has been sent.')})
    
    def send_reset_password_email(self, user):
        context = {
            'email': user.email,
            'domain': djoser_settings.get('DOMAIN') or self.request.get_host(),
            'site_name': djoser_settings.get('SITE_NAME'),
            'uid': utils.encode_uid(user.pk),
            'user': user,
            'token': utils.default_token_generator.make_token(user),
            'protocol': 'http',
            'url_reset_password': reverse('password_reset_confirm'),
        }
        subject_template_name = 'password_reset_subject.txt'
        email_template_name = 'password_reset_email.html'
        subject = loader.render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        email = loader.render_to_string(email_template_name, context)
        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email])