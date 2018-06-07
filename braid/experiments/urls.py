from django.urls import path
from . import views

app_name = 'experiments'
urlpatterns = [
    # /experiment/upload-file
    path('upload-file/', views.upload_file, name='upload'),
]
