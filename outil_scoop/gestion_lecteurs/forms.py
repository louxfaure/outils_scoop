from django import forms
from bootstrap_datepicker_plus import DatePickerInput

class LecteurForm(forms.Form):
    identifiant = forms.CharField(label="Saisissez l'identifiant du compte",max_length=100, required=True)

class ChangeLecteurForm(forms.Form):
    nouvel_identifiant = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "name": "nouvel_identifiant"}),
        required=False
        )
    date_expiration =  forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y',
        attrs={"name":"date_expiration"}),
        required=False
        )