import strawberry
from typing import List
from .types import Fruit


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
