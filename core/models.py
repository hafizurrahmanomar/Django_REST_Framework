
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from app import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extras):
        if email == '':
            raise ValueError("Email address not provided")

        user = self.model(email=email, **extras)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extras):
        if email == '':
            raise ValueError("Email address not provided")
        user = self.model(email=email, **extras)
        user.set_password(password)
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name