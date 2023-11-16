from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model representing the user of the system
    """

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name"]
    EMAIL_FIELD = "email"

    date_joined = models.DateTimeField(
        default=now,
        verbose_name="Joined on",
        help_text="Date and time when the user was created",
    )
    username = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Username",
        help_text="Username (must be unique)",
    )
    email = models.EmailField(
        max_length=255,
        verbose_name="Email",
        help_text="User's email address (optional)",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this user should be treated as active",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Staff",
        help_text="Whether this user has access to the admin site",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="User's full name",
    )

    objects = UserManager()

    def __str__(self):
        return str(self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
  


