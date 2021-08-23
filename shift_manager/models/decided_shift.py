from django.db import models

from shift_manager.models.user import User
from shift_manager.models.store import Store

class DecidedShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    date = models.DateField()
    starting_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + ' : ' + str(self.date)
