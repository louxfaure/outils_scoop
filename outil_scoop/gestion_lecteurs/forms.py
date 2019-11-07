from django import forms

class LecteurForm(forms.Form):
    identifiant = forms.CharField(label="Saisissez l'identifiant du compte",max_length=100, required=True)