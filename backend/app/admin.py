from django.contrib import admin
from .models import ImageModel

@admin.register(ImageModel)
class ImageModel(admin.ModelAdmin):
    pass
