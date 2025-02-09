from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

# class AgentForm(forms.ModelForm):
#     class Meta:
#         model = Agent
#         fields = (
#             'user',
#             'organization',
#         )

#     def clean_user(self):
#         user = self.cleaned_data.get('user')
#         # Prevent creating an agent with a user that's already an agent
#         if Agent.objects.filter(user=user).exists():
#             raise forms.ValidationError("This user is already an agent.")
#         return user