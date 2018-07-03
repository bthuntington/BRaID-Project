from django import forms
from .models import File
from django.forms.widgets import CheckboxSelectMultiple
from . import utils

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment', 'document', 'description', ]


class PickAnalysisForm(forms.ModelForm):

    OPTIONS = ()
    selected_analysis = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    class Meta:
        model = File
        fields = []

    # TODO: get options relevant to file
    # method not working, with options_list variable in views

    def __init__(self, *args, **kwargs):
        super(PickAnalysisForm, self).__init__(*args, **kwargs)
        # get options for file
        file_type = self.instance.mimetype_type

        options_list = utils.set_analysis_options(self.instance.mimetype_type)
        if len(options_list) > 0:
            # build tuple out of choices
            for opt in options_list:
                self.OPTIONS = self.OPTIONS + (opt, )
            print("OPtions: ", self.OPTIONS)
        else:
            # tell user there are no avaliable options
            self.OPTIONS = (('NONE', 'No analysis options'),)

        # reassign field with new values
        self.fields['selected_analysis'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, choices=self.OPTIONS)
