from django.shortcuts import render, redirect
from .models import File
from .forms import FileUploadForm

def file_list(request):
    files = File.objects.filter()
    return render(request, 'files/file/list.html', {'files': files})

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.save()
            return redirect('files:file_list')
    else:
        form = FileUploadForm()
    return render(request, 'files/file/upload.html', {'form': form})
