from django.urls import path, include
from . import views

urlpatterns = [
    path('file', views.upload_file_view, name='upload_file'),
    path('image', views.upload_image, name='upload_image'),
]


