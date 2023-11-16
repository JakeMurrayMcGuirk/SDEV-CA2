from rest_framework import routers
from django.urls import path
from .views import UserViewSet, home, signup, user_login, user_logout, user_profile, user_settings, user_preferences, account_deletion, dashboard
users_router = routers.SimpleRouter()
users_router.register(r"users/user", UserViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('settings/', user_settings, name='settings'),
    path('preferences/', user_preferences, name='preferences'),
    path('delete/', account_deletion, name='account_delete'),
    path('dashboard/', dashboard, name='dashboard'),
]

urlpatterns += users_router.urls