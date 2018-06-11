from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from braid.settings import MEDIA_ROOT
import magic
from Bio import SeqIO

# view to upload files
# uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save(commit=False)

            # read in file in chunk
            handle_uploaded_file(request.FILES['file_file'])

            # automatically add path
            file_model.path = file_model.file_file.path

            # get file mimetype/mimetype type
            mimetype = magic.from_file(file_model.path, mime=True)
            # print("magic mimetype: ", mimetype)

            # assign mimetype for text mimetypes
            if "text" in mimetype.lower():
                file_model.mimetype,file_model.mimetype_type = is_text(file_model.file_file.path)

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
    # ? store at path variable?
    filename = new_file.name
    with open(MEDIA_ROOT + new_file.name, 'wb+') as destination:
        for chunk in new_file.chunks():
            destination.write(chunk)

def is_text(path):
    mimetype = "Text"
    # assume .txt as default type
    mimetype_type = "txt"

    # check other text mimetype types
    if check_if_fasta(path):
        mimetype_type = "fasta"

    print("Mimetype {} type {}".format(mimetype,mimetype_type))
    return mimetype, mimetype_type

def check_if_fasta(text_file_path):
    """ parse fasta file using Biopython and return false if
    anything does not fit """
    with open(text_file_path, 'rU') as handle:
        return any(SeqIO.parse(handle, "fasta"))
