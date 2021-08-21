from django.db import models
from django.utils import timezone



class User(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)
    store_id = models.CharField(verbose_name='店舗',max_length=50)
    name = models.CharField(verbose_name='名前', max_length=50)
    email = models.CharField(verbose_name='Eメール', max_length=50)
    password = models.CharField(verbose_name='パスワード', max_length=100)
    score = models.CharField(verbose_name='点数', max_length=50)
    role = models.CharField(verbose_name='役割', max_length=50)
    is_staff = models.CharField(max_length=50)
    is_superuser = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=50)
	
    def __str__(self):
     return self.name
