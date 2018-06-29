from django import forms
from .models import File
#, Analysis
from django.forms.widgets import CheckboxSelectMultiple


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment', 'file_file', 'file_description', ]


# TODO: display no analysis message if there are no analysis
class FileAnalysisForm(forms.models.ModelForm):

    class Meta:
        model = File
        fields = ['analysis_information']

    def __init__(self, *args, **kwargs):
        super(FileAnalysisForm, self).__init__(*args, **kwargs)

        self.fields['analysis_information'].widget = CheckboxSelectMultiple()
        self.fields['analysis_information'].queryset = Analysis.objects.filter(
            parent_file_id=self.instance.pk)
        #self.fields['analysis_information'].required = False
