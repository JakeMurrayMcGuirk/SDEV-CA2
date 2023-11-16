from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['preferences']