from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    headline = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)

    # username = models.CharField(max_length=50, unique=False,null=True,blank=True)
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.birth_date.year

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
