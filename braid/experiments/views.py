from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from braid.settings import MEDIA_ROOT
import magic
from Bio import SeqIO


# view to upload files, uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save(commit=False)

            # read in file in chunk
            handle_uploaded_file(request.FILES['file_file'])

            # automatically add path
            file_model.path = file_model.file_file.path

            # automatically get file name
            file_model.file_name = file_model.file_file.name

            # get file mimetype/mimetype type
            magic_mimetype = magic.from_file(file_model.path, mime=True)

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
                text_type = is_text(file_model.path)
                if (text_type, text_type) in file_model.MIMETYPE_TYPE:
                    file_model.mimetype_type = text_type
            else:
                file_model.mimetype_type = 'unknown'

            print("All info: \n\texperiment: {} \n\tpath: {} \n\tmimetype: \
                    {} \n\tmimetype type: {} \n\tname: {} \n\tdescription: {}\
                  \n\tfile: {}".format(file_model.experiment, file_model.path,
                                       file_model.mimetype,
                                       file_model.mimetype_type,
                                       file_model.file_name,
                                       file_model.file_description,
                                       file_model.file_file))

            # Save to model
            file_model.save()

            # TODO: Change to more meaningful page
            return HttpResponse("Valid form. File commited.")
    else:
        form = UploadFileForm()
    # TODO: spot for testing request returns what it's supposed to
    return render(request, 'experiments/upload_file.html', {'form': form})


# write file in chuncks, not all at once
def handle_uploaded_file(new_file):
    with open(MEDIA_ROOT + '/' + new_file.name, 'wb+') as destination:
        for chunk in new_file.chunks():
            destination.write(chunk)


def is_text(path):
    mimetype_type = str()

    # check other text mimetype types
    if check_if_fasta(path):
        mimetype_type = "fasta"
    else:
        # default is txt
        mimetype_type = "txt"

    return mimetype_type


def check_if_fasta(text_file_path):
    # parse fasta file using Biopython and return false if
    # anything does not fit
    with open(text_file_path, 'rU') as handle:
        return any(SeqIO.parse(handle, "fasta"))
