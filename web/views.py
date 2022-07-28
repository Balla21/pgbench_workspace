from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import generate_file
# Create your views here.
def index(request):
    return render(request, "index.html")

def file_scripting(request):
    filename = request.POST.get('filename')
    dbname = request.POST.get('databasename')
    file = generate_file(filename, dbname)
    return redirect('index')
