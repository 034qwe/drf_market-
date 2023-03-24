
from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('articles/', ArticlesApiList.as_view()),
    path('articles/<int:pk>/',ArticlesAPIUpdate.as_view()),
    path('articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('category/<slug:cat_slug>/',ShowCategoryApiList.as_view() ,name='category'),
    path('all_category/',CategoryArticlesApiList.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('cart/', CartApiList.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartAPIUpdate.as_view(), name='cart-detail'),
    path('cart/<int:pk>/', CartAPIDestroy.as_view())
]
