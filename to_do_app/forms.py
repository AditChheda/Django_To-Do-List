from django import forms
from django.forms.widgets import TextInput, Textarea

class AddItem(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=Textarea)
    priority = forms.IntegerField()