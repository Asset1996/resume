from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""
    email = models.EmailField("Email address", max_length=255, unique=True)
    name = models.CharField("Name of the user", max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'



class WorkExperience(models.Model):
    """Model that describes work experience of the user"""
    class Meta():
        ordering = ['end_date']
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Name of the user")
    company_name = models.CharField(max_length=50, verbose_name="Name of the company")
    position = models.CharField(max_length=50, verbose_name="Position of the user")
    start_date = models.DateField(verbose_name="The date when the user started working")
    end_date = models.DateField(default=None, blank=True, null=True, verbose_name="The date when the user ended working")
    work_description = models.CharField(default=None, blank=True, null=True, max_length=250, verbose_name="Brief work description")

    def __str__(self) -> str:
        return self.position

