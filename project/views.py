from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count

from .models import Project
from .models import Update
from .models import Role

# Create your views here.
def index(request):

    queryset = Project.objects.annotate(num_members=Count('members'))

    title = request.GET.get("title", None)
    if title: 
        queryset = queryset.filter(project_title__contains=title)
    
    stage = request.GET.get("stage", None)
    if stage: 
        queryset = queryset.filter(stage=stage)

    members = request.GET.get("members", None)
    if members:
        if int(members) == 1: # 1-5
            queryset = queryset.filter(num_members__gte=1, num_members__lte=5)
        if int(members) == 2: # 5-10
            queryset = queryset.filter(num_members__gt=5, num_members__lte=10)
        if int(members) == 3: # 10-20
            queryset = queryset.filter(num_members__gt=10, num_members__lte=20)
        if int(members) == 4: # 20+
            queryset = queryset.filter(num_members__gt=20)

    roles = request.GET.get("roles", None)
    if roles: 
        role_ids = Role.objects.filter(role_title__contains=roles)
        # project_list = Role.objects.filter
        print(role_ids)

    tags = request.GET.get("tags", None)
    if tags: 
        queryset = queryset.filter(tags__tag_title__contains=tags)
    
    context = {
        'latest_projects': queryset,
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