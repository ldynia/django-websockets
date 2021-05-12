# schema.py

import graphene

from django.contrib.auth.models import User
from graphene_django import DjangoObjectType


class UserObjectType(DjangoObjectType):

    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserObjectType)
    hello = graphene.String(description='A typical hello world')

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_hello(self, info):
        return 'World'


class Subscription():
    pass


schema = graphene.Schema(query=Query)