from django.contrib import admin
from models import timeevent
# Register your models here.
class TimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(timeevent, TimeAdmin)
