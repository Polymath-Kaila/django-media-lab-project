from django.db import models

class UploadFileModel(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
