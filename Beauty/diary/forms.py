from django import forms
from .models import Post,Note
from ..courses.models import Course
from ..treatments.models import Treatment



class PostPractitionerForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treatment'].queryset = Treatment.objects.filter(user=user)
        self.fields['course'].queryset = Course.objects.filter(user=user)


# class PostClientForm(PostPractitionerForm):
#     class Meta(PostPractitionerForm.Meta):
#         exclude = ['user', 'treatment', 'course']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['treatment'] = forms.ModelChoiceField(queryset=Treatment.objects.none())  # Placeholder field
#         self.fields['course'] = forms.ModelChoiceField(queryset=Course.objects.none())  # Placeholder field
#         self.fields['treatment'].widget = forms.HiddenInput()
#         self.fields['course'].widget = forms.HiddenInput()
class PostClientForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user','course','treatment']



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
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].disabled = True
        self.fields['course'].disabled = True
        self.fields['treatment'].disabled = True

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
