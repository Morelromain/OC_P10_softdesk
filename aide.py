# Permission de Projet
class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # Permission si Utilisateur est authentifié pour /projet/
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Permission si Utilisateur = auteur du projet pour /projet/num
        return obj.author_user_id == request.user


class ProjectViewSet(viewsets.ModelViewSet):
    ''' '''

    def get_queryset(self):
        # Récupère les projets de l'Utilisateur uniquement
        user = self.request.user 
        return Project.objects.filter(author_user_id=user)


class IssueViewSet(viewsets.ModelViewSet):
    ''' '''

    def get_queryset(self, *args, **kwargs):
        # Récupère les Erreurs du Projet de l'URL uniquement
        project = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project)


class ProjectViewSet(viewsets.ModelViewSet):
# est égal à :
class ProjectViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):


    def has_object_permission(self, request, view, obj):
        # Soit update/delete si autheur soit lecture
        print("TESTESTESTEST") 
        print (request.method)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author_user_id == request.user