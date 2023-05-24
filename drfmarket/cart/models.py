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
    owner = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='purchase')
    cartorder_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Cartitems,on_delete=models.CASCADE, null=True,related_name='product_order')

    def __str__(self):
        return f"cart={self.owner}"

#### короче ідея зробити карт ордер так само як карт геть потім ще одну модеть ордеркарт
#  як карт ітем тіки вже замість продукта буде екземпляр кат ітема а замість карт карт ордер
# і квантіті нафіг не треба то буду робити завтра написав щоб не забути!!!
