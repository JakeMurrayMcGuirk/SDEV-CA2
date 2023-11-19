from django import forms
from .models import User, UserPreferences, UserProfile
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Validate password against Django's built-in validators
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return password


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['option1', 'option2', 'option3']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']