from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','body','category','image']
        exclude = ['created_at']



class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','body','category','image']
        exclude = ['created_at','updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True


class CourseDeleteForm(forms.ModelForm):
    # Add any additional fields if needed
    class Meta:
        model = Course
        fields = ['title','body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
