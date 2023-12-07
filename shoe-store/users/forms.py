from django import forms
from .models import User, UserPreferences, UserProfile

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name']


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

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'age', 'gender', 'phone_number']