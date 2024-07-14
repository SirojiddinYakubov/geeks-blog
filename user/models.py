from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import CustomUserManager


class CustomUser(AbstractUser):
    identifier = models.CharField(max_length=40, unique=True)

    avatar = models.ImageField(upload_to="users/avatars", null=True, blank=True)
    headline = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @property
    def name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.birth_date.year

    USERNAME_FIELD = "identifier"
    objects = CustomUserManager()
