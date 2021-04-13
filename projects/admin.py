from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Project, Contributor, Issue, Comment


admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment) 