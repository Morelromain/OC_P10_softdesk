from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .models import Project, Contributor, User, Issue, Comment


admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(User, UserAdmin)
admin.site.register(Issue)
admin.site.register(Comment)