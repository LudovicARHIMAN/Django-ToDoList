from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Label", max_length=200)