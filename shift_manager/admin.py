from django.contrib import admin
from shift_manager.models.decided_shift import DecidedShift
from shift_manager.models.hoped_shift import HopedShift
from shift_manager.models.store import Store
from shift_manager.models.user import User

class UserAdmin(admin.ModelAdmin):
    fields = ['store', 'name', 'email', 'score', 'role', 'is_staff', 'is_superuser']

# Register your models here.
admin.site.register(DecidedShift)
admin.site.register(HopedShift)
admin.site.register(Store)
admin.site.register(User, UserAdmin)