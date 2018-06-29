from django import forms
from .models import File
from django.forms.widgets import CheckboxSelectMultiple


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['experiment', 'file_file', 'description', ]


class PickAnalysisForm(forms.ModelForm):

    OPTIONS = (('ex1', 'example 1'), ('ex2','example 2'))
    selected_analysis = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    class Meta:
        model = File
        fields = []

    # TODO: get options relevant to file
    # method not working, with options_list variable in views
    """
    def __init__(self, *args, **kwargs):
        super(PickAnalysisForm, self).__init__(*args, **kwargs)
        # if potential analysis, add them to user's choices
        options_list = kwargs.pop['options_list']
        if len(options_list) > 0:
            # build tuple out of choices
            for opt in options_list:
                self.OPTIONS = self.OPTIONS + (opt, )
        else:
            # tell user there are no avaliable options
            self.OPTIONS = (('NONE', 'No analysis options'),)

        # reset selected_analysis field with new options
        self.fields['selected_analysis'] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple, choices=self.OPTIONS)
    """
