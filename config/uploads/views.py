from django.shortcuts import render, redirect
from .forms import FileUploadForm, ImageUploadForm

def upload_file_view(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = FileUploadForm()

    return render(request, 'uploads/file_upload.html', {'form': form})

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageUploadForm()
        
    return render(request, 'uploads/image_upload.html', {'form': form})