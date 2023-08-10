from django.contrib.auth import get_user_model
from django.db import models
from Beauty.courses.models import Course
from Beauty.diary.models import Post
from Beauty.treatments.models import Treatment

# Create your models here.
"""
The field Comment Text is required:
• Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
• Date and Time of Publication - when a comment is created (only), the date of publication is automatically
generated
"""

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True,blank=True)
    to_post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True,blank=True)
    to_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE,null=True,blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Like(models.Model):
    to_course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True,blank=True)
    to_post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True )
    to_treatment = models.ForeignKey(Treatment,on_delete=models.CASCADE, null=True,blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
