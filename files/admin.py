from django.contrib import admin
from django.contrib.admin import ModelAdmin

from files.models import File


@admin.register(File)
class FileAdmin(ModelAdmin):
    list_display = ('original_filename', 'file_extension', 'mime_type', 'description')
    search_fields = ('original_filename', 'description')

