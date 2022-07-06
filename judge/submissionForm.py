from django.forms import ModelForm
from django import forms
from .models import Submission

class codeForm(ModelForm):
    code = forms.CharField(widget = forms.Textarea)
    class  Meta:
        model = Submission
        fields = ['code']