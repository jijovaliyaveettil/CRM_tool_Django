from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'name',
            'email',
            'phone_number',
            'age',
            'agent'
        )   

class LeadForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    age = forms.IntegerField()