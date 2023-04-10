from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register('allcarts', CartAllViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('cartuser/', CartUserAPIList.as_view()),
    path('cartuserdelete/<int:pk>/', CartUserAPIDestroy.as_view()),
    path('carts/',CartAllAPIView.as_view()),
    path('cartadd/',CartAPICreate.as_view()),
    path('cartitemsadd/', CartItemsUserApiAdd.as_view()),
]


#я хотел сыграть на кери но зашел в сапер, и теперь сижу в таверне я в таверне.... что ж спою 

#ну а я ковбой мое ранчо меня ждет