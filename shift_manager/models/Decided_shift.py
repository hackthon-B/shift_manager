from django.db import models
from django.utils import timezone

class Decided_shift(models.Model):
    id = models.IntegerField(verbose_name='ID',primary_key=True)
    user_id = models.IntegerField()
    store_id = models.IntegerField()
    year = models.DateField()
    month = models.DateField()
    day = models.DateField()
    starting_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.CharField(max_length=50)

    def __str__(self):
     return self.name
