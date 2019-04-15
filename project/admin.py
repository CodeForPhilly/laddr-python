from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Tag
from .models import Profile
from .models import Update
from .models import Role

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Update)
admin.site.register(Role)
