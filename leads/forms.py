from django import forms

class LeadForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    age = forms.IntegerField()