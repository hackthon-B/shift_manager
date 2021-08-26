from django.db import models

from shift_manager.models.user import User
from shift_manager.models.store import Store

class HopedShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    work = models.BooleanField(verbose_name='出勤可・不可', max_length=50)
    date = models.DateField()
    starting_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + ' : ' + str(self.date)
