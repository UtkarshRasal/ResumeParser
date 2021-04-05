import os

def file_path(request):
    if request.method == 'POST':
        path = os.path.join("/tmp", request.FILES['file'].name)
        with open(path, "wb") as fp:
            fp.write(request.FILES['file'].read())  
        
        return path