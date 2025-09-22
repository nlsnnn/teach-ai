from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("teacher", "Учитель"),
        ("admin", "Админ"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='teacher')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
