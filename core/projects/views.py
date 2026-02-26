from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def projects(request):
    template_name = 'projects/projects.html'
    all_projects = models.Project.objects.all()
    context = { 'projecs': all_projects }
    return render(request, template_name, context)


def project(request, pk):
    template_name = 'projects/single-project.html'
    single_project = models.Project.objects.get(id=pk)
    tags = single_project.tags.all()
    context = {
        'pk': pk,
        'project': single_project,
        'tags': tags,
    }
    return render(request, template_name, context)


def create_project(request):
    template_name = 'projects/project-form.html'
    form = forms.ProjectForm()

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {'form': form}
    return render(request, template_name, context)


def update_project(request, pk):
    project = models.Project.objects.get(id=pk)
    template_name = 'projects/project-form.html'
    form = forms.ProjectForm(instance=project)

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:projects')

    context = {'form': form}
    return render(request, template_name, context)
