from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        labels = {
            'comment_text': 'Comment',
        }
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',

                },
            )
        }

