from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    THEME_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
    )
    LANG_CHOICES = (
        ('en', 'English'),
        ('ru', 'Русский'),
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    theme = models.CharField(
        max_length=10, choices=THEME_CHOICES, default='light')
    language = models.CharField(
        max_length=2, choices=LANG_CHOICES, default='ru')
