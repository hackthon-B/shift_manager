from django.db import models
from django.utils import timezone

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
    is_active = models.CharField(max_length=50)

    def __str__(self):
     return self.name
