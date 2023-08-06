from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from Beauty.accounts.models import BeautyUser

UserModel = get_user_model()



class RegisterUserForm(auth_forms.UserCreationForm):
    consent = forms.BooleanField()
    group = forms.ChoiceField(choices=[])
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            excluded_group_names = ['admins']
            groups = Group.objects.exclude(name__in=excluded_group_names)
            self.fields['group'].choices = [(group.id, group.name) for group in groups]

            self.fields['username'].help_text = 'This will be used for login.'
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text = ''
            self.fields['password2'].label = 'Repeat password'

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2', 'consent','group')

    widgets = {
        'username': forms.TextInput(attrs={
            'placeholder': 'Username',
        }),
        'email': forms.EmailInput(attrs={
            'placeholder': 'Enter valid email',
        }),
    }

    def save(self, commit=True):
        result = super().save(commit)
        return result


class BeautyUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'

class BeautyUserEditForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['username','first_name','last_name','address','profile_picture','bio','gender','phone']


class DeleteAppUserForm(AuthenticationForm):
    username = forms.CharField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Your password"}), label='')

    class Meta:
        model = UserModel
        fields = ["username", "password"]



class DeleteBeautyUserForm(AuthenticationForm):
    username = forms.CharField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Your password"}), label='')

    class Meta:
        model = UserModel
        fields = ["username", "password"]
