from django.urls import path
from . import views

urlpatterns = [
    path('file', views.upload_file, name='upload_file'),
    path('image', views.upload_image, name='upload_image'),
]