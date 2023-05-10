from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

import uuid


from main.models import Articles

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    user_cart = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')


    def __str__(self):
        return str(self.id)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items', blank=True, null=True)
    product = models.ForeignKey(Articles, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=1)


class CartOrder(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='purchase')
    cartorder_date = models.DateTimeField(auto_now_add=True)
    product1 = models.ForeignKey(Cartitems, on_delete=models.CASCADE, blank=True, null=True, related_name='product1')

    def __str__(self):
        return f"Purchase {self.id}"