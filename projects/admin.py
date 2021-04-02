from django.contrib import admin

# Register your models here.

from .models import Project, Contributor, User, Issue, Comment


admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(User)
admin.site.register(Issue)
admin.site.register(Comment)