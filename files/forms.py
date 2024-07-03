from django.forms import Form, ModelForm
from .models import File

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['file', 'description']