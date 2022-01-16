import random
import strawberry
import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations
from typing import List
from .types import (
    Color, 
    Fruit,
    FruitFilter,
    FruitInput
)
from . import models


greetings = ["hi", "hello", "안녕"]
def resolve_hello(root, info) -> str:
    return random.choice(greetings)


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=resolve_hello)
    fruit: Fruit = strawberry_django.field()
    fruits: List[Fruit] = strawberry_django.field(filters=FruitFilter)
    # fruits: List[Fruit] = strawberry.field(resolver=resolve_fruit)
    color: Color = strawberry_django.field()
    colors: List[Color] = strawberry_django.field()


@strawberry.type
class Mutation:
    createFruit: Fruit = mutations.create(FruitInput)


schema = strawberry.Schema(query=Query)
