"""laddr-python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from project import views as main_views

urlpatterns = [
    path('', main_views.homepage),
    path('mission', main_views.mission),
    path('conduct', main_views.conduct),
    path('team', main_views.team),
    path('contact', main_views.contact),
    path('projects/', include('project.urls')),
    path('admin/', admin.site.urls),
]
