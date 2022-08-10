from django.urls import path
from .views import index, file_scripting


urlpatterns = [
    path('', index, name='index'),  # the empty route path will call the view function index for execution

    path('generation/', file_scripting),  # the generation route path will call the view function file_scripting
]