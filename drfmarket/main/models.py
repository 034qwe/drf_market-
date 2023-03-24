from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Articles(models.Model):
    title=models.CharField('title',max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    categ = models.ForeignKey('Category_Articles',on_delete=models.PROTECT,) #+= _id
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")
    user = models.ForeignKey(User,verbose_name='user',on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title


class Category_Articles(models.Model):
    name = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug':self.slug})

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Articles)
    created_at = models.DateTimeField(auto_now_add=True)