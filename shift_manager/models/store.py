from django.db import models
from django.utils import timezone

class Store(models.Model):
    name = models.CharField(verbose_name='名前', max_length=50)
    business_stating_time = models.TimeField()
    business_closing_time = models.TimeField()
    closing_sunday = models.BooleanField(default=False)
    closing_monday = models.BooleanField(default=False)
    closing_tuesday = models.BooleanField(default=False)
    closing_wednesday = models.BooleanField(default=False)
    closing_thursday = models.BooleanField(default=False)
    closing_friday = models.BooleanField(default=False)
    closing_saturday = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

