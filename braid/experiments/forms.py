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

    def __init__(self, *args, **kwargs):
        super(PickAnalysisForm, self).__init__(*args, **kwargs)

        # get options for file
        options_list = utils.set_analysis_options(self.instance.mimetype_type)
        if len(options_list) > 0:
            # build tuple out of choices
            for opt in options_list:
                self.OPTIONS = self.OPTIONS + ((opt, opt), )
            print("OPtions: ", self.OPTIONS)
        else:
            # tell user there are no avaliable options
            self.OPTIONS = ('No Analysis Options', 'No Analysis Options')

        # reassign field with new values
        self.fields['selected_analysis'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, choices=self.OPTIONS)
