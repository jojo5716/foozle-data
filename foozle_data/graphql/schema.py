import graphene

from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from .user import UserQuery
from .navigation import NavigationQuery
from .project import ProjectQuery

class Query(UserQuery, NavigationQuery, ProjectQuery):
    debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(query=Query)

