from django.shortcuts import render, redirect
from django.http import HttpResponse

from .utils import generate_file, execute_file # local module need for view function

# Create your views here.
def index(request):
    ''' This view function is called when a request has been made towards the homepage of the web app '''
    return render(request, "index.html")

def file_scripting(request):
    '''
        This view function is called through submitting a post request from the form in
        order the run script based on the filename, database name, timing and scaling factor
    '''

    filename = request.POST.get('filename')
    dbname = request.POST.get('databasename')
    timing = request.POST.get('timing')
    scaling = request.POST.get('scaling')
    file = generate_file(filename, dbname, timing, scaling)
    result = execute_file(file)
    if len(result) > 1:
        context = {"output": result}
        return render(request, "output.html", context)
    else :
        return redirect('index')