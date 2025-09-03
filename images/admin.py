from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url", "description"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]


