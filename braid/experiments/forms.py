from django import forms
from .models import File, Analysis
from django.forms.widgets import CheckboxSelectMultiple


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment', 'file_file', 'file_description', ]


class FileAnalysisForm(forms.models.ModelForm):
    class Meta:
        model = File
        fields = ['analysis_information']

    def __init__(self, *args, **kwargs):
        super(FileAnalysisForm, self).__init__(*args, **kwargs)

        self.fields['analysis_information'].widget = CheckboxSelectMultiple()
        self.fields['analysis_information'].queryset = Analysis.objects.all()
