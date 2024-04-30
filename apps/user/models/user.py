from django.db import models
from apps.game.models.category import Category
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Username must be set')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password)
        user.is_superuser = True
        user.is_staff = True  # is_staff ni True qiling
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class User(AbstractBaseUser, PermissionsMixin):  # PermissionsMixin ni qo'shing
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # is_staff ni qo'shing

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username

class History(models.Model):
    count = models.IntegerField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField()
    is_win = models.BooleanField()