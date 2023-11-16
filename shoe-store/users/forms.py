from django import forms
from .models import User, UserPreferences

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['option1', 'option2', 'option3']