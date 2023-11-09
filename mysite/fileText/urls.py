from django.urls import path
from . import views

urlpatterns = [path("upload-file", views.upload_file, name='upload_file'),
               path("show-file", views.show_file, name='show_file')]
