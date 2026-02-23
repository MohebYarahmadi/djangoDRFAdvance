from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def projects(request):
    template_name = 'projects/projects.html'
    context = {
        'first_name': 'John',
        'last_name': 'Doe',
    }
    return render(request, template_name, context)


def project(request, pk):
    template_name = 'projects/single-project.html'
    context = {
        'pk': pk,
        'title': 'My Game',
        'budget': '5M',
    }
    return render(request, template_name, context)
