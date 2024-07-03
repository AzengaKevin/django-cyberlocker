
from files.models import File


def run():
    
    files = File.objects.all()
    
    files = files.filter(mime_type__startswith='image')
    
    for (index, file) in enumerate(files):
        print(index, file.mime_type)