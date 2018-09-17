import graphene
from graphene_django import DjangoObjectType


from ..apps.data.models import Project  


class Projects(DjangoObjectType):
    class Meta:
        model = Project


class ProjectQuery(graphene.ObjectType):
    get_all_projects = graphene.List(Projects)
    get_project_by_id = graphene.Field(Projects, id=graphene.String())

    def resolve_get_all_projects(self, args):
        return Project.objects.all()

    def resolve_get_project_by_id(self, args, **kwargs):
        try:
            return Project.objects.get(unique_id=kwargs["id"])
        except (Project.DoesNotExist, KeyError):
            return None
