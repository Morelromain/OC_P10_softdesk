from django.urls import include, path
from rest_framework_nested import routers
'''from rest_framework import routers'''
from projects import views

from django.contrib import admin
from django.urls import path


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'contributor', views.ContributorViewSet)
'''router.register(r'issue', views.IssueViewSet)'''

router.register(r'project', views.ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
project_router.register(r'issue', views.IssueViewSet, basename='project-issue')

issue_router = routers.NestedSimpleRouter(project_router, r'issue', lookup='issue')
issue_router.register(r'comment', views.CommentViewSet, basename='issue-comment')

router.register(r'comment', views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]


'''"""softdesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]'''
