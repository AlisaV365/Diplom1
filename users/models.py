from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', ('member')
    MODERATOR = 'moderator', ('moderator')


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    city = models.CharField(max_length=235, verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram', **NULLABLE)

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
