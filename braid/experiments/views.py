from django.shortcuts import render
from .forms import UploadFileForm, FileAnalysisForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from .models import File
import magic
from Bio import SeqIO


# Show information and give options once upload complete
class UploadSuccessView(UpdateView):
    model = File
    form_class = FileAnalysisForm
    template_name = 'experiments/upload_success.html'


# view to upload files, uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save(commit=False)

            # automatically add path
            file_model.path = file_model.file_file.path

            # automatically get file name
            file_model.file_name = file_model.file_file.name

            # find temporary path to work with
            temp_path = request.FILES['file_file'].temporary_file_path()

            # get file mimetype/mimetype type
            magic_mimetype = magic.from_file(temp_path, mime=True)
            mimetype = magic_mimetype.split('/')[0].capitalize()

            # check if mimetype matches a known mimetype
            if (mimetype, mimetype) in file_model.MIMETYPE:
                file_model.mimetype = mimetype
            else:
                file_model.mimetype = 'Unknown'

            mimetype_type = magic_mimetype.split('/')[1].lower()
            # check if type exists in list
            if (mimetype_type, mimetype_type) in file_model.MIMETYPE_TYPE:
                file_model.mimetype_type = mimetype_type
            elif 'text' in file_model.mimetype.lower():
                # check for other type text if necessary
                if 'plain' in mimetype_type:
                    text_type = is_plain_text(temp_path)
                    if (text_type, text_type) in file_model.MIMETYPE_TYPE:
                        file_model.mimetype_type = text_type
                # unknown text type to database
                else:
                    file_model.mimetype_type = 'unknown'
            elif 'jpeg' in mimetype_type:
                # catch images where jpeg not jpg
                file_model.mimetype_type = 'jpg'
            else:
                file_model.mimetype_type = 'unknown'

            file_model.get_analysis_types()
            """
            print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: {}\
                \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
                \n\tfile: {}".format(file_model.experiment, file_model.path,
                                     file_model.mimetype,
                                     file_model.mimetype_type,
                                     file_model.file_name,
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


def is_plain_text(path):
    mimetype_type = 'unknown'

    # 'extension' : (MIMETYPE_TYPE, boolean to verify extension)
    is_type = {'.csv': ('csv', True), '.txt': ('txt', True),
               '.fasta': ('fasta', check_if_fasta(path))}

    # get file extension, assume follows last .
    if len(path.split('.')) > 1:
        extension = '.' + path.split('.')[-1].lower()

    # determine if it is a known extension
    if extension in is_type:
        if is_type[extension][1]:
            mimetype_type = is_type[extension][0]

    return mimetype_type


def check_if_fasta(text_file_path):
    # parse fasta file using Biopython and return false if
    # anything does not fit
    with open(text_file_path, 'rU') as handle:
        return any(SeqIO.parse(handle, "fasta"))
