from django.core.validators import ValidationError


def letters(value):
    if not value.isalpha():
        raise ValidationError("Name can contain only letters!")