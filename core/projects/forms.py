from django.forms import ModelForm
from . import models

class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'demo_link', 'source_link', 'tags']
