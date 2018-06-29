from django.shortcuts import render
from .forms import UploadFileForm, PickAnalysisForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from .models import File
from . import utils


class RunAnalysisView(DetailView):
    model = File
    template_name = 'experiments/run_analysis.html'


from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

class SelectAnalysisView(UpdateView):  # SingleObjectMixin, FormView):
    template_name = 'experiments/upload_success.html'
    form_class = PickAnalysisForm
    model = File

    # TODO: Verify form

# view to upload files, uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save(commit=False)

            # automatically get file name
            file_model.name = file_model.file_file.name

            # find temporary path to work with
            temp_path = request.FILES['file_file'].temporary_file_path()
            file_model.mimetype, file_model.mimetype_type = utils.get_mimetype_fields(
                temp_path, file_model)

            """
            print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
                \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
                \n\tfile: {}".format(file_model.experiment, file_model.path,
                                     file_model.mimetype,
                                     file_model.mimetype_type,
                                     file_model.name,
                                     file_model.file_description,
                                     file_model.file_file))
            """

            # Save to model
            file_model.save()

            # easier when testing file upload
            # return HttpResponse("Valid form. File commited.")
            return HttpResponseRedirect(reverse('experiments:success',
                                                args=(file_model.id,)))
    else:
        form = UploadFileForm()
    # TODO: spot for testing request returns what it's supposed to
    return render(request, 'experiments/upload_file.html', {'form': form})
