from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Treatment(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    photo_treatment = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title

