from enum import Enum

from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models

class Gender(Enum):
    MALE= 1
    FEMALE = 2
    DO_NOT_SHOW = 3

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

# Create your models here.
class BeautyUser(auth_models.AbstractUser):
    MIN_LENGTH = 2
    MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=(validators.MinLengthValidator(MIN_LENGTH),),)

    last_name = models.CharField(
        max_length=MAX_LENGTH,
        validators=(validators.MinLengthValidator(MIN_LENGTH),),)

    email= models.EmailField(
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
        validators=(validators.MinLengthValidator(MIN_LENGTH),),
    )
    bio = models.TextField(
        max_length=400,
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return f'{self.username}'
