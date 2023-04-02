from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register('allcarts', CartAllViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('cartuser/', CartUserAPIView.as_view()),
    path('cartuserdelete/<int:pk>/', CartUserDeleteAPIView.as_view()),
    path('carts/',CartAllAPIView.as_view())

]




#ну а я ковбой мое ранчо меня ждет