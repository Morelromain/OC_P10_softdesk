from django.urls import include, path
from django.contrib import admin

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects import views
from users import views as users_views

router = routers.DefaultRouter()
'''router.register(r'users', views.UserViewSet)'''
# Project
router.register(r'project', views.ProjectViewSet)
# For Issue and Contributor
project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
# Issue
project_router.register(r'issue', views.IssueViewSet, basename='project-issue')
# Contribor (users)
project_router.register(r'users', views.ContributorViewSet, basename='project-contributor')
# For Comment
issue_router = routers.NestedSimpleRouter(project_router, r'issue', lookup='issue')
# Comment
issue_router.register(r'comment', views.CommentViewSet, basename='issue-comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
