from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse

# view to upload files
# uses UploadFileForm
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_model = form.save()
            return HttpResponse("Valid form. File commited.")
    else:
        form = UploadFileForm()
    # TODO: spot for testing request returns what it's supposed to
    return render(request, 'experiments/upload_file.html', {'form': form})

# write file in chuncks, not all at once
def handle_uploaded_file(new_file, filename):
    # ? store at path variable?
    with open('files/' + filename, 'wb+') as destination:
        for chunk in new_file.chunks():
            destination.write(chunk)
