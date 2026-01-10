from django.db import models

class UploadFileModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/') # no validation, accepts any file type
    uploaded_at = models.DateTimeField(auto_now_add=True)


class UploadedImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/') # validates image files
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
