from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import SignupForm, UserSettingsForm, UserPreferencesForm, ProfilePictureForm, UserProfileForm
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# View for the homepage
def home(request):
    return render(request, 'home.html')

def signup(request):
    form = SignupForm(request.POST) if request.method == 'POST' else SignupForm()
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']

        user = User.objects.create_user(username, email=email, name=name, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Failed to create user')

    return render(request, 'signup.html', {'form': form})

# View for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect accordingly
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'login.html')

# View for user logout
@login_required
def user_logout(request):
    logout(request)
    # Redirect to homepage or login page
    return redirect('home')



# View for user account settings
@login_required
def user_settings(request):
    user = request.user
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully')
    else:
        form = UserSettingsForm(instance=user)
    
    return render(request, 'settings.html', {'form': form})


# View for user preferences
@login_required
def user_preferences(request):
    user = request.user
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Preferences updated successfully')
    else:
        form = UserPreferencesForm(instance=user)
    
    return render(request, 'preferences.html', {'form': form})

# View for user account deletion
@login_required
def account_deletion(request):
    user = request.user
    if request.method == 'POST':
        # Logic to delete user account
        user.delete()
        messages.success(request, 'Account deleted successfully')
        return redirect('home')
    
    return render(request, 'account_delete.html', {'user': user})


@login_required
def user_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            # Redirect or handle success
    else:
        profile_form = UserProfileForm(instance=user_profile)

    return render(
        request,
        'profile.html',
        {'user': user, 'user_profile': user_profile, 'profile_form': profile_form}
    )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = ProfilePictureForm()

    return render(request, 'profile.html', {'form': form})