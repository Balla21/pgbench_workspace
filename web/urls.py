from django.urls import path
from .views import index, file_scripting


urlpatterns = [
    path('', index, name='index'),
    path('generation/', file_scripting)
]