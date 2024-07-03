from django.urls import path, include
from .views import file_list, file_upload

app_name = 'files'

urlpatterns = [
    path('upload/', file_upload, name='file_upload'),
    path('', file_list, name='file_list'),
]