from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project
from .models import Update
from .models import Role

# Create your views here.
def index(request):
    latest_projects = Project.objects.all()
    context = {
        'latest_projects': latest_projects,
    }
    return render(request, 'project/index.html', context)

def details(request, project_id):
    project = Project.objects.get(pk=project_id)
    updates = Update.objects.filter(project=project_id)
    roles = Role.objects.filter(project=project_id)
    context = {
        'project': project,
        'updates': updates,
        'roles': roles,
    }
    return render(request, 'project/details.html', context)

def homepage(request):
    return render(request, 'project/homepage.html')