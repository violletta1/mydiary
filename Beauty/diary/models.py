
from django.contrib.auth import get_user_model
from django.db import models
from Beauty.courses.models import Course
from Beauty.treatments.models import Treatment

UserModel = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)



class Note(models.Model):
    CHOICES = {
        'rad': 'rad',
        'good': 'good',
        'meh': 'meh',
        'bad': 'bad',
        'awful': 'awful'
    }
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=20,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    feelings = models.CharField(max_length=10, choices=[choice for choice in CHOICES.items()])

    image = models.URLField(null=True, blank=True)

    to_do_list = models.TextField(null=True,blank=True)
    remainder = models.CharField(max_length=30, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title