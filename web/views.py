from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import generate_file
# Create your views here.
def index(request):
    return render(request, "index.html")

def file_scripting(request):
    filename = request.POST.get('filename')
    dbname = request.POST.get('databasename')
    timing = request.POST.get('timing')
    scaling = request.POST.get('scaling')
    file = generate_file(filename, dbname, timing, scaling)
    return redirect('index')
