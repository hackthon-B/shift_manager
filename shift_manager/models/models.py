from django.db import models
from django.utils import timezone



class User(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)
    store_id = models.CharField(verbose_name='店舗',max_length=50)
    name = models.CharField(verbose_name='名前', max_length=50)
    password = models.CharField(verbose_name='パスワード', max_length=100)
    score = models.CharField(verbose_name='点数', max_length=50)
    role = models.CharField(verbose_name='役割', max_length=50)
    is_staff = models.CharField()
    is_superuser = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=50)
    hoped_shift = models.ForeignKey(Hoped_shift, on_delete=models.CASCADE)
    decided_shift = models.ForeignKey(Decided_shift, on_delete=models.CASCADE)
	def __str__(self):
        return self.name

class Store(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)
    name = models.CharField(verbose_name='名前', max_length=50)
    business_stating_time = models.DateTimeField()
    business_closing_time = models.DateTimeField()
    closing_sunday = models.DateTimeField()
    closing_monday = models.DateTimeField()
    closing_tuesday = models.DateTimeField()
    closing_wednesday = models.DateTimeField()
    closing_thursday = models.DateTimeField()
    closing_friday = models.DateTimeField()
    closing_saturday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hoped_shift = models.ForeignKey(Hoped_shift, on_delete=models.CASCADE)      
    decided_shift = models.ForeignKey(Decided_shift, on_delete=models.CASCADE)

	 def __str__(self):
        return self.name

class Hoped_shift(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    cannot_work = models.CharField(verbose_name='出勤不可', max_length=50)
    year = models.DateTField()
    month = models.DateField()
    day = models.DateField()
    starting_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField()

	def __str__(self):
        return self.name    

class Decided_shift(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)   
    user_id = models.IntegerField()                                   
    store_id = models.IntegerField()     
    year = models.DateTField()
    month = models.DateField()
    day = models.DateField()
    starting_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField()

	def __str__(self):
        return self.name
