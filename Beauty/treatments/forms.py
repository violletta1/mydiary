from django import forms
from .models import Treatment

class TreatmentAddForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
        exclude = ['user']

class TreatmentEditForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
