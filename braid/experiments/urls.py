from django.urls import path
from . import views

app_name = 'experiments'
urlpatterns = [
    # /experiment/upload-file
    path('upload-file/', views.upload_file, name='upload'),
    # view file upload info
    path('<int:pk>/success/', views.SelectAnalysisView.as_view(),
         name='success'),
    # load when running analysis
    path('<int:pk>/analysis/', views.RunAnalysisView.as_view(),
         name='analysis_info'),
    # allows creation of new experiment
    path('upload-file/file_information/', views.index,
         name='file_information'),

]
