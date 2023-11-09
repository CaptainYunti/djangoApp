from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .word_mixer import WordMixer
import os


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            WordMixer(request.FILES["file"])
            return HttpResponseRedirect("/file-text/show-file")
    else:
        form = UploadFileForm()
    return render(request, "simple_upload.html", {"form": form})


def show_file(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'mixed-words.txt')

    with open(file_path, 'r') as file_read:
        text = file_read.read()
    return HttpResponse(text, content_type="text/plain")

