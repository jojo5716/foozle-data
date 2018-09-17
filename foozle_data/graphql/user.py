import graphene
from graphene_django import DjangoObjectType


from ..apps.data.models import UserProfile


class User(DjangoObjectType):
    class Meta:
        model = UserProfile


class UserQuery(graphene.ObjectType):
    get_all_users = graphene.List(User)
    get_user_by_id = graphene.Field(User,id=graphene.String())

    def resolve_get_all_users(self, args):
        return UserProfile.objects.all()

    def resolve_get_user_by_id(self, args, **kwargs):
        try:
            return UserProfile.objects.get(unique_id=kwargs["id"])
        except (UserProfile.DoesNotExist, KeyError):
            return None
