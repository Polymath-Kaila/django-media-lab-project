from django import models
from .models import UploadFileModel, UploadedImageModel

class FileUploadForm(models.Model):
    class Meta:
        model = UploadFileModel
        fields = ['title', 'file']

class ImageUploadForm(models.Model):
    class Meta:
        model = UploadedImageModel
        fields = ['title', 'image']
