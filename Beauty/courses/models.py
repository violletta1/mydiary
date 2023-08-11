from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Course(models.Model):
    CHOICES = {
        'face': 'face',
        'body':'body',
        'hair':'hair'
    }
    title = models.CharField(max_length=20,null=False,blank=False)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=False,blank=False)

    body = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=4, choices=[choice for choice in CHOICES.items()])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.URLField(null=True,blank=True,)

    def __str__(self):
        return self.title

