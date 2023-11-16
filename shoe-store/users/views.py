from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
from .forms import SignupForm, UserSettingsForm, UserPreferencesForm
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


# View for the homepage
def home(request):
    return render(request, 'home.html')

# View for user signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate page after signup
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = SignupForm()
    
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
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'login.html')

# View for user logout
@login_required
def user_logout(request):
    logout(request)
    # Redirect to homepage or login page
    return redirect('home')

# View for user profile
@login_required
def user_profile(request):
    user = request.user
    # Fetch user profile data
    profile = UserProfile.objects.get(user=user)
    return render(request, 'profile.html', {'user': user, 'profile': profile})

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
    
    return render(request, 'account_deletion.html', {'user': user})

# View for the dashboard
@login_required
def dashboard(request):
    user = request.user
    # Logic to display user dashboard (e.g., orders, cart)
    
    return render(request, 'dashboard.html', {'user': user})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer