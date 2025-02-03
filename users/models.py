from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)  # Ensure username is unique
    first_name = models.CharField(max_length=150, blank=True, null=True)  # Optional
    last_name = models.CharField(max_length=150, blank=True, null=True)  # Optional

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
