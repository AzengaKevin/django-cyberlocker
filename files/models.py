from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
import mimetypes
import os

User = get_user_model()

class File(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    original_filename = models.CharField(max_length=255, blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    file_extension = models.CharField(max_length=10, blank=True, null=True)
    mime_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original_filename

    def save(self, *args, **kwargs):
        if not self.original_filename:
            self.original_filename = self.file.name
        if not self.file_extension:
            self.file_extension = os.path.splitext(self.file.name)[1]
        if not self.mime_type:
            self.mime_type, _ = mimetypes.guess_type(self.file.name)
        super().save(*args, **kwargs)

