from enum import Enum

from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import models as auth_models
from Beauty.accounts.validators import letters


class Gender(Enum):
    MALE= 1
    FEMALE = 2
    DO_NOT_SHOW = 3

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class BeautyUser(auth_models.AbstractUser):

    MIN_LENGTH = 2
    MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=[MinLengthValidator(MIN_LENGTH),letters],)

    last_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=[MinLengthValidator(MIN_LENGTH),letters],)

    email = models.EmailField(
        unique=True,
    )
    gender = models.IntegerField(
        choices=Gender.choices(),
        default=Gender.DO_NOT_SHOW.value,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=MAX_LENGTH,
        validators=(MinLengthValidator(MIN_LENGTH),),
    )
    bio = models.TextField(
        max_length=400,
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return f'{self.username}'

