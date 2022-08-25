"""
Models page for main app.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """
    Manager for users.
    Need to customize to override the create_user and 
    create_superuser by email field (not username).
    """
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
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User name")
    company_name = models.CharField(max_length=50, verbose_name="Company name")
    position = models.CharField(max_length=50, verbose_name="Position of the user")
    start_date = models.DateField(verbose_name="The date when the user started working")
    end_date = models.DateField(default=None, blank=True, null=True, verbose_name="The date when the user ended working")
    work_description = models.CharField(default=None, blank=True, null=True, max_length=250, verbose_name="Brief work description")

    def __str__(self) -> str:
        return self.position


class Education(models.Model):
    """Model that describes the education of the user"""
    types = (
        ('un', 'University'), 
        ('cl', 'College'), 
        ('cl', 'Certification'), 
    )
    degrees = (
        ('ms', 'Masters'), 
        ('bc', 'Bachelors'), 
        ('hs', 'High school'), 
        ('ms', 'No degree'), 
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User name")
    institution_name = models.CharField(max_length=50, verbose_name="Institution name")
    speciality = models.CharField(max_length=50, verbose_name="Specialty of user")
    type = models.CharField(max_length=50, verbose_name="Type of education", choices=types)
    degree = models.CharField(max_length=50, verbose_name="Students degree", choices=degrees)
    start_date = models.DateField(verbose_name="The date when the user started")
    end_date = models.DateField(default=None, blank=True, null=True, verbose_name="The date when the user graduated")
    course_description = models.CharField(default=None, blank=True, null=True, max_length=250, verbose_name="Brief study description")

    class Meta():
        ordering = ['end_date']

    def __str__(self) -> str:
        return self.degree
