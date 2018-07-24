from django.urls import path
from . import views

app_name = 'experiments'
urlpatterns = [
    # Welcome page
    path('welcome/', views.welcome_page, name='welcome'),
    # /experiment/upload-file
    path('welcome/upload-file/', views.upload_file, name='upload'),
    # view file upload info
    path('<int:pk>/success/', views.SelectAnalysisView.as_view(),
         name='success'),
    # load when running analysis
    path('<int:pk>/analysis/', views.RunAnalysisView.as_view(),
         name='analysis_info'),
    # allows creation of new experiment
    path('welcome/upload-file/file_information/', views.get_name,
         name='file_information'),
    # shows all experiments, authors, and files
    path('welcome/upload-file/overview/', views.get_experiments,
        name='overview')
]
