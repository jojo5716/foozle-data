import graphene
from graphene_django import DjangoObjectType


from ..apps.data.models import Navigation, Page 

class PageType(DjangoObjectType):
    class Meta:
        model = Page

class Navigations(DjangoObjectType):
    all_pages = graphene.List(PageType, id=graphene.String())

    @graphene.resolve_only_args
    def resolve_all_pages(self, args="", **kwargs):
        return self.pages.all()

    class Meta:
        model = Navigation



class NavigationQuery(graphene.ObjectType):
    get_all_navigations = graphene.List(Navigations)
    get_navigations_by_user = graphene.Field(Navigations,id=graphene.String())

    def resolve_get_all_navigations(self, args):
        return Navigation.objects.all()

    def resolve_get_navigations_by_user(self, args, **kwargs):
        try:
            return Navigation.objects.filter(user__unique_id=kwargs["user"])
        except KeyError:
            return []