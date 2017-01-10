from django.contrib import admin
from models import Photo
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photo, GalleryAdmin)
