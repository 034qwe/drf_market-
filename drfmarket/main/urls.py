
from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('api/v1/articles/', ArticlesApiList.as_view()),
    path('api/v1/articles/<int:pk>/',ArticlesAPIUpdate.as_view()),
    path('api/v1/articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()),
    # path('category/<slug:cat_slug>/',ShowCategoryApiList.as_view() ,name='category')
]
