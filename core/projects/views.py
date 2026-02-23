from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def projects(request):
    template_name = 'projects/projects.html'
    return render(request, template_name)


def project(request):
    template_name = 'projects/single-project.html'
    return render(request, template_name)
