
from django.shortcuts import render


def is_allowed_group_user(user):
    allowed_groups = ['admins', 'clients','practitioners']  # List of allowed group names
    return user.groups.filter(name__in=allowed_groups).exists()


def is_admin_group_user(user):
    allowed_groups = ['admins', ]
    return user.groups.filter(name__in=allowed_groups).exists()


def is_client_group_user(user):
    allowed_groups = ['clients', 'admins']
    return user.groups.filter(name__in=allowed_groups).exists()

def is_practitioner_group_user(user):
    allowed_groups = ['practitioners', 'admins']
    return user.groups.filter(name__in=allowed_groups).exists()