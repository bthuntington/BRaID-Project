from django.shortcuts import render
from .forms import UploadFileForm, PickAnalysisForm, AuthorForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from . import utils
from .models import File, Experiment, Author


class RunAnalysisView(DetailView):
    model = File
    template_name = 'experiments/run_analysis.html'


class SelectAnalysisView(UpdateView):  # SingleObjectMixin, FormView):
    template_name = 'experiments/upload_success.html'
    form_class = PickAnalysisForm
    model = File

    def form_valid(self, form):
        analysis = form.cleaned_data.get('selected_analysis')
        print("Anlysis to be run include: ", analysis)
        # utils.make_analysis(analysis)
        # return super().form_valid(form)

        # for now just print out the analysis type
        return_string = "running analysis: " + str(analysis)
        return HttpResponse(return_string)


# view to upload files, uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save(commit=False)

            # automatically get file name
            file_model.name = file_model.document.name

            # find temporary path to work with
            temp_path = request.FILES['document'].temporary_file_path()
            results = utils.get_mimetype_fields(temp_path, File)
            file_model.mimetype, file_model.mimetype_type = results

            """
            print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
                \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
                \n\tfile: {}".format(file_model.experiment, file_model.path,
                                     file_model.mimetype,
                                     file_model.mimetype_type,
                                     file_model.name,
                                     file_model.file_description,
                                     file_model.document))
            """

            # Save to model
            file_model.save()

            # easier when testing file upload
            # return HttpResponse("Valid form. File committed.")
            return HttpResponseRedirect(reverse('experiments:success',
                                                args=(file_model.id,)))
    else:
        form = UploadFileForm()
    # TODO: spot for testing request returns what it's supposed to
    return render(request, 'experiments/upload_file.html', {'form': form})


def welcome_page(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('experiments:upload'))
    return render(request, 'experiments/welcome.html')

def get_name(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if (request.POST.get('first_name') and request.POST.get('last_name')):
            first = request.POST['first_name']
            last = request.POST['last_name']
            auth = Author(first_name=first, last_name=last)
            auth.save()
        elif form.is_valid():
            auth = form.cleaned_data['authors']
            #elif(form.is_valid()):
            #Incomplete

        if(request.POST.get('name') and request.POST.get('condition')):
            name = request.POST['name']
            condition = request.POST['condition']
            ex = Experiment(name=name, condition=condition, author=auth)
            #saves new experiment to database
            ex.save()
            return HttpResponseRedirect(reverse('experiments:upload'))

    return render(request, 'experiments/file_information.html',
        {'form': form})

def get_experiments(request):
    experiments = Experiment.objects.all()
    files = File.objects.all()
    context = {
        'experiments' : experiments,
        'files' : files
    }
    return render(request, 'experiments/overview.html', context)

