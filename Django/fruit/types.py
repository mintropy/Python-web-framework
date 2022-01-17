import strawberry
import strawberry_django
from strawberry.django import auto
from django.contrib.auth import get_user_model
from typing import List
from . import models


# filter
# @strawberry.django.type(models.Fruit)
@strawberry_django.filters.filter(models.Fruit, lookups=True)
class FruitFilter:
    id: auto
    name: auto
    color: 'ColorFilter'


# @strawberry.django.type(models.Color)
@strawberry_django.filters.filter(models.Color, lookups=True)
class ColorFilter:
    id: auto
    name: auto
    fruits: FruitFilter


# order
@strawberry_django.ordering.order(models.Fruit)
class FruitOrder:
    name: auto
    color: 'ColorOrder'


@strawberry_django.ordering.order(models.Color)
class ColorOrder:
    name: auto
    fruit: FruitOrder


# types
@strawberry_django.type(
    models.Fruit, filters=FruitFilter, order=FruitOrder, pagination=True
)
class Fruit:
    id: auto
    name: auto
    color: 'Color'


@strawberry_django.type(
    models.Color, filters=ColorFilter, order=ColorOrder, pagination=True
)
class Color:
    id: auto
    name: auto
    color: List[Fruit]


@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto


# input types
@strawberry_django.input(models.Fruit)
class FruitInput:
    id: auto
    name: auto
    color: auto