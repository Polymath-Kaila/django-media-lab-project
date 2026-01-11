from django import forms
from .models import UploadFileModel, UploadedImageModel

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['title', 'file']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImageModel
        fields = ['title', 'image']
