from django import forms

class AtomForm(forms.Form):
    atomList = forms.CharField()
