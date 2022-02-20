from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('user must have a email')
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        superuser = self.create_user(
            email=email,
            password=password,
        )
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractUser):
    email = models.CharField(max_length=128, unique=True)
    username = models.CharField(max_length=64, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'account'
