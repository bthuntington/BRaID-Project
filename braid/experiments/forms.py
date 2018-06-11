from django import forms
from .models import File

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment','file_file','file_description',]
