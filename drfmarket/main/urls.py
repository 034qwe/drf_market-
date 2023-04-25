
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import *




urlpatterns = [
    path('articles/', ArticlesApiList.as_view()),
    path('articles/<int:pk>/',ShowArticlesApiList.as_view()),
    path('articlesupdate/<int:pk>/',ArticlesAPIUpdate.as_view()),
    path('articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    path('category/<slug:cat_slug>/',ShowCategoryApiList.as_view() ,name='category'),
    path('all_category/',CategoryArticlesApiList.as_view()),
    path('drf-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
     path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
