from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import magic
from braid.settings import MEDIA_ROOT

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

            # get file type
            if "text" in mimetype.lower():
                file_model.mimetype = is_text(file_model.file_file.path)

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
    check_if_fasta(path)
    # for now just return Text
    return "Text"

def check_if_fasta(text_file_path):
    # TODO: use Biopython to determine if fasta file
    pass

