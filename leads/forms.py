from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField }

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