from django import forms
from .models import Post,Note
from ..courses.models import Course
from ..treatments.models import Treatment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

class PostClientForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','treatment','course']

class PostPractitionerForm(PostForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','course']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True

class PostEditPractitionerForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True

class PostEditClientForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','treatment','course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
class PostDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
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


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['user']


class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['created_at','updated_at','user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True


class NoteDeleteForm(forms.ModelForm):
    # Add any additional fields if needed
    class Meta:
        model = Note
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
