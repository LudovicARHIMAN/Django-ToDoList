from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

class AddItems(forms.Form):
    text = forms.CharField(label="Text", max_length=200)
