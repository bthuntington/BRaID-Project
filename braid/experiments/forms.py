from django import forms
from .models import File
from django.forms.widgets import CheckboxSelectMultiple


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment', 'file_file', 'description', ]

class PickAnalysisForm(forms.Form):
    options_list = []
    def __init__(self,options_list,*args,**kwargs):
        super(PickAnalysisForm,self).__init__(*args,**kwargs)
        self.options_list = options_list #kwargs.pop('options_list')
    OPTIONS = ()
    if len(options_list) > 0:
        # build tuple out of choices
        for opt in options_list:
           OPTIONS = OPTIONS + (opt,)
    else:
        OPTIONS = ('NONE', 'No analysis options')

    selected_analysis = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
