from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from .views import *

router = routers.DefaultRouter()
router.register('carts', CartViewSet)

urlpatterns = [
    path('',include(router.urls))

]




#ну а я ковбой мое ранчо меня ждет